#!python

import multiprocessing as mp
import pickle, glob, os, subprocess, argparse, datetime, \
    time, re, shutil, tarfile, gzip, copy, sys, random
from bigmcl.lib.utils import collect_files, expandEnvVar, formatPath, \
    vprint, eprint, intro, outro, zprint, findExecs


def runWC(file_):
    with open(file_, 'r') as raw:
        return sum(1 for line in raw)
#    check_lines = subprocess.run([
 #       'wc', '-l', file_
  #      ], stdout = subprocess.PIPE
   #     )
    #return int(check_lines.stdout.decode('utf-8').rstrip().split(' ')[0])


def rmZeros(row_file, mtx_dir):

    zeros = {}
    with open(row_file + '.tmp', 'w') as out:
        with open(row_file, 'r') as raw:
            for line in raw:
                entries = line.rstrip().split('\t')
                if not entries[2:]:
                    init = int(line[:line.find('\t')])
                    zeros[init] = line
                else:
                    vals = [int(x.split(':')[0]) for x in entries]
                    for x in vals:
                        if x in zeros:
                            out.write(zeros[x])
                            del zeros[x]
                    out.write(line)

    os.rename(row_file + '.tmp', row_file)
    with open(mtx_dir + 'zeros.txt', 'w') as out:
        out.write('\n'.join([str(x) for x in list(zeros)]))

    return zeros


def createSubgraphsAsym(row_file, mtx_dir, index):

    # must start from lowest index first and progress for this function to work
    graph_file = mtx_dir + 'sub.' + str(index) + '.mtx'
    hits, old_hits = set(), {index}
    with open(graph_file + '.tmp0', 'w') as out:
        with open(row_file, 'r') as raw:
            for line in raw:
                init = int(line[:line.find('\t')])
                if init == index:
                    entries = line.rstrip().split('\t')
                    for entry in entries[2:]:
                        info = [x for x in entry.split(':')]
                        out.write(str(init) + ' ' + info[0] + ' ' + info[1] + '\n')
                        hit = int(info[0])
#                        if hit not in zeros: # it wouldn't be a zero if it was in another
                        hits.add(int(info[0]))
                    break

        all_hits = hits.union(old_hits)
        cont, other_hits = True, set()
        while hits or cont:
            if other_hits == hits and hits: #either an error or the file was changed
#                print('\tERROR: value(s) without rows ' + str(hits), flush = True)
 #               sys.exit(17)
                old_hits = set()
                break
            other_hits = copy.deepcopy(hits)
            cont = False
            with open(row_file, 'r') as raw:
                for line in raw:
                    init = int(line[:line.find('\t')])
                    entries = line.rstrip().split('\t')
                    info = [x.split(':') for x in entries[2:]]
                    if init in hits or any(int(x[0]) in all_hits for x in info):
                        if init not in old_hits:
                            cont = True
                            for d in info:
                                hit = int(d[0])
                                if hit not in old_hits:
                                    out.write(str(init) + ' ' + d[0] + ' ' + d[1] + '\n')
#                                    if hit not in zeros:
                                    hits.add(hit)
                                    all_hits.add(hit)
                            old_hits.add(init)
                            all_hits.add(init)
                            if init in hits:
                                hits.remove(init)

    if len(old_hits) > 1:
        min_hit = min(list(old_hits))
        with open(mtx_dir + 'sub.' + str(min_hit) + '.old_hits.txt', 'w') as out:
            out.write('\n'.join([str(x) for x in old_hits]))
        os.rename(graph_file + '.tmp0', mtx_dir + 'sub.' + str(min_hit) + '.mtx.tmp1')
    else:
        os.remove(graph_file + '.tmp0')

    return old_hits 


def createSubgraphsSym(row_file, mtx_dir, index):

    graph_file = mtx_dir + 'sub.' + str(index) + '.mtx'
    # must start from lowest index first and progress for this function to work
    hits, old_hits = set(), {index}
    with open(graph_file + '.tmp0', 'w') as out:
        with open(row_file, 'r') as raw:
            for line in raw:
                init = int(line[:line.find('\t')])
                if init == index:
                    entries = line.rstrip().split('\t')
                    for entry in entries[2:]:
                        info = [x for x in entry.split(':')]
                        out.write(str(init) + ' ' + info[0] + ' ' + info[1] + '\n')
                        hits.add(int(info[0]))
                    break

        while hits:
            with open(row_file, 'r') as raw:
                for line in raw:
                    init = int(line[:line.find('\t')])
                    if init in hits:
                        entries = line.rstrip().split('\t')
                        for entry in entries[2:]:
                            info = [x for x in entry.split(':')]
                            hit = int(info[0])
                            if hit not in old_hits:
                                out.write(str(init) + ' ' + info[0] + ' ' + info[1] + '\n')
                                hits.add(hit)
                        old_hits.add(init)
                        hits.remove(init)

    if len(old_hits) > 1:
        min_hit = min(list(old_hits))
        with open(mtx_dir + 'sub.' + str(min_hit) + '.old_hits.txt', 'w') as out:
            out.write('\n'.join([str(x) for x in old_hits]))
        os.rename(graph_file + '.tmp0', mtx_dir + 'sub.' + str(min_hit) + 'mtx.tmp1')
    else:
        os.remove(graph_file + '.tmp0')

    return old_hits


def prep_mcl(graph_file, sym = True, output = subprocess.DEVNULL):

    prep_file = re.sub(r'\.tmp$', '', graph_file)
    if sym:
        conv_pipe = subprocess.call([
            'mcxload', '-abc', graph_file, '-o', prep_file,
            '--write-binary', '-write-tab',
            re.sub(r'\.mtx$', '.tsv', prep_file), '--stream-mirror'
            ], stdout = output, stderr = output #, stdin = subprocess.PIPE
            )
    else:
        conv_pipe = subprocess.call([
            'mcxload', '-abc', graph_file, '-o', prep_file,
            '--write-binary', '-write-tab',
            re.sub(r'\.mtx$', '.tsv', prep_file)
            ], stdout = output, stderr = output #, stdin = subprocess.PIPE
            )
    return prep_file


def conv_clus(clus_file, output = subprocess.DEVNULL):

    conv_cmd = subprocess.call([
        'mcxdump', '-icl', clus_file + '.tmp',
        '-o', clus_file, '--dump-pairs'
        ], stdout = output,
        stderr = subprocess.DEVNULL
        )
    os.remove(clus_file + '.tmp')


def run_mcl(
    graph_file, clus_file, inflation, 
    cpus = 1, sym = True, output = subprocess.DEVNULL
    ):

    vprint('\t\tRunning ' + os.path.basename(clus_file), flush = True, v = not output)
    prep_file = prep_mcl(graph_file, sym)
    os.remove(graph_file)
    mcl_cmd = subprocess.call([
        'mcl', prep_file, '-o', clus_file + '.tmp',
        '-I', str(inflation), '-te', str(cpus)],
        stdout = subprocess.DEVNULL, stderr = output
        )
    conv_clus(clus_file)


def reload_subgraph(mtx_dir, row_file, complete_file, zero_file):
    with open(complete_file, 'r') as raw:
        old_indices = set([int(x[:x.find('\t')]) for x in raw])
#        old_indices = set([int(x.rstrip()) for x in raw])
    if os.path.isfile(zero_file):
        with open(zero_file, 'r') as raw:
            zeros = set([int(x.rstrip()) for x in raw])
    else:
        zeros = set()
    with open(row_file + '.tmp', 'w') as out:
        with open(row_file, 'r') as raw:
            for line in raw:
                d = int(line[:line.find('\t')])
                if d in old_indices:
                    continue
                out.write(line)
    os.rename(row_file + '.tmp', row_file)

    return old_indices, zeros


def subgraphMngr(
    clusters, mtx_dir, row_file, 
    old_indices = set(), sym = True, zeros = {}, cpus = 2
    ):

    cpus -= 1
    complete_file, procs, to_run = mtx_dir + 'complete.txt', [], []
    # 0 is often the largest cluster, so let's start here
    if sym:
        procs.append(mp.Process(
            target = createSubgraphsSym,
            args=(row_file, mtx_dir, 0, zeros)
            ))
    else:
        procs.append(mp.Process(
            target=createSubgraphsAsym,
            args=(
                row_file, mtx_dir, 0
                )
            ))
    procs[-1].start() 

    clus_range = list(range(1, clusters))
    random.shuffle(clus_range)
    for i0 in clus_range:
        if i0 not in old_indices:
            while len(procs) == cpus:
                todel = []
                for i1, proc in enumerate(procs):
                    if not proc.is_alive():
                        todel.append(i1)
                        proc.join()
                done_subgraphs = collect_files(mtx_dir, 'mtx.tmp1')
                for subgraph in done_subgraphs:
                    old_file = re.sub(r'mtx.tmp1$', 'old_hits.txt', subgraph)
                    with open(old_file, 'r') as raw:
                        rec_old_indices = set([int(x.rstrip()) for x in raw])
                    old_indices = old_indices.union(rec_old_indices)
                    with open(row_file + '.tmp', 'w') as row_out:
                        with open(row_file, 'r') as raw:
                            with open(complete_file, 'a') as comp_out: 
                                for line in raw:
                                    d = int(line[:line.find('\t')])
                                    if d in rec_old_indices:
                                        comp_out.write(line)
                                        continue
                                    row_out.write(line)
                    os.rename(row_file + '.tmp', row_file)
                    os.rename(subgraph, subgraph[:-1])

                for i1 in reversed(todel):
                    procs.pop(i1)
                    
            if sym:
                procs.append(mp.Process(
                    target = createSubgraphsSym,
                    args=(row_file, mtx_dir, i0, zeros)
                    ))
                procs[-1].start()
            else:
                procs.append(mp.Process(
                    target=createSubgraphsAsym,
                    args=(
                        row_file, mtx_dir, i0
                        )
                    ))
                procs[-1].start() 


def mclMngr(
    subgraph_proc, processes, mtx_dir, inflation, 
    sym = True, output = subprocess.DEVNULL
    ):

    complete_prep = collect_files(mtx_dir, 'clus')
    complete = set([re.sub(r'clus$', 'mtx.tmp', x) for x in complete_prep])

    procs = []
#    init_mtx = mtx_dir + 'sub.0.mtx.tmp'
 #   if os.path.isfile(init_mtx):
  #      clus = mtx_dir + 'sub.0.clus'
   #     init_proc = mp.Process(
    #        target=run_mcl,
     #       args=(
      #          init_mtx, clus,
       #         inflation, 2, sym, output
        #        )
         #   )
#        init_proc.start()
 #       init_proc.join()
  #      complete.add(init_mtx)
#    elif not os.path.isfile(init_mtx[:-4]):
 #       print('\t\tWARNING: No connections from index 0. Is this true?', flush = True)

    while subgraph_proc.is_alive():
        to_del = []
        for i, proc in enumerate(procs):
            if not proc.is_alive():
                to_del.append(i)
        for entry in reversed(to_del):
            procs[entry].join()
            del procs[entry]

        mtx_files = collect_files(mtx_dir, '[0-9]*.mtx.tmp')
        to_run = [x for x in mtx_files if x not in complete]
        while len(procs) < 1:
            try:
                mtx = to_run[0]
            except IndexError:
                break
            clus = re.sub(r'\.mtx.tmp$', '.clus', mtx)
            procs.append(mp.Process(
                target=run_mcl,
                args=(mtx, clus, inflation, 2, sym, output)
                ))
            complete.add(mtx)
            procs[-1].start()
            del to_run[0]
        time.sleep(1)

    subgraph_proc.join()
    mtx_files = collect_files(mtx_dir, '[0-9]*.mtx.tmp')
    to_run = [x for x in mtx_files if x not in complete]

    while to_run or procs:
        to_del = []
        for i, proc in enumerate(procs):
            if not proc.is_alive():
                to_del.append(i)
        for entry in reversed(to_del):
            procs[entry].join()
            del procs[entry]
        while len(procs) < processes and to_run:
            mtx = to_run[0]
            clus = re.sub(r'\.mtx.tmp$', '.clus', mtx)
            procs.append(mp.Process(
                target=run_mcl,
                args=(mtx, clus, inflation, 2, sym, output)
                ))
            procs[-1].start()
            complete.add(mtx)
            del to_run[0]
        time.sleep(1)


def clusteringMngr(
    cluster_len, row_file, mtx_dir, inflation, cpus, 
    sym = True, output = subprocess.DEVNULL
    ):

    zeros, complete_file = {}, mtx_dir + 'complete.txt'
    if os.path.isfile(complete_file):
        old_indices, zeros = reload_subgraph(
            mtx_dir, row_file, complete_file, mtx_dir + 'zeros.txt'
            )
    else:
        zeros, old_indices = set(), set()
        if not sym:
            zeros = rmZeros(row_file, mtx_dir)
#            old_indices = createSubgraphsAsym(row_file, mtx_dir, 0)
 #           old_indices = old_indices.union(zeros)
                 
  #      with open(row_file + '.tmp', 'w') as out:
   #         with open(row_file, 'r') as raw:
    #            for line in raw:
     #               d = int(line[:line.find('\t')])
      #              if d in old_indices:
       #                 continue
        #            out.write(line)
       # os.rename(row_file + '.tmp', row_file)

    subgraph_proc = mp.Process(
        target = subgraphMngr, 
        args = (cluster_len, mtx_dir, row_file, old_indices, sym, zeros, cpus)
        )
    subgraph_proc.start()
    mclMngr(subgraph_proc, cpus - 1, mtx_dir, inflation, sym, output)


def clusteringMngrSingle(cluster_len, row_file, mtx_dir, inflation, sym = True, output = subprocess.DEVNULL):

    zeros = None
    if sym:
        old_indices = createSubgraphsSym(row_file, mtx_dir, 0)
        if os.path.isfile(mtx_dir + 'sub.0.mtx.tmp1'):
            os.rename(mtx_dir + 'sub.0.mtx.tmp1', mtx_dir + 'sub.0.mtx')
    else:
        zeros = rmZeros(row_file)
        old_indices = createSubgraphsAsym(row_file, mtx_dir, 0)
        old_indices = old_indices.union(zeros)
        if os.path.isfile(mtx_dir + 'sub.0.mtx.tmp1'):
            os.rename(mtx_dir + 'sub.0.mtx.tmp1', mtx_dir + 'sub.0.mtx')

    to_run = []
    for i in range(1, cluster_len):
        if i not in old_indices:
            mtx_file, clus_file = mtx_dir + str(i) + '.mtx', mtx_dir + str(i) + '.clus'
            old_indices = old_indices.union(
                createSubgraphsSym(row_file, mtx_dir, i)
                )
            if os.path.isfile(mtx_dir + 'sub.' + str(i) + '.mtx.tmp1'):
                os.rename(mtx_dir + 'sub.' + str(i) + '.mtx.tmp1', mtx_dir + 'sub.' + str(i) + '.mtx')
                to_run.append(mtx_file, clus_file)

    for files in to_run:
        run_mcl(files[0], files[1], inflation, 2, sym, output)


def readSubclusters(mtx_dir, out_dir, clusLen):

    master_file = mtx_dir + 'labels.tsv'
    clus_files = collect_files(mtx_dir, '[0-9]*.clus')

    master_conv = {}
    if os.path.isfile(master_file):
        with open(master_file, 'r') as raw:
            for line in raw:
                data = [int(x) for x in line.rstrip().split('\t')]
                master_conv[data[0]] = data[1]

    clusters = []
    for clus_file in clus_files:
        sub_file = re.sub(r'\.clus$', '.tsv', clus_file)
        t_clus = {}
        with open(clus_file, 'r') as raw:
            for line in raw:
                data = [int(x) for x in line.rstrip().split('\t')]
                if data[0] not in t_clus:
                    t_clus[data[0]] = []
                t_clus[data[0]].append(data[1])

        t_conv = {}
        with open(sub_file, 'r') as raw:
            for line in raw:
                data = [int(x) for x in line.rstrip().split('\t')]
                t_conv[data[0]] = data[1]

        init_conv = [
            [t_conv[y] for y in t_clus[x]] for x in t_clus
            ]
        if master_conv:
            conv_clus = [
                [master_conv[y] for y in x] for x in init_conv
                ]
            clusters.extend(conv_clus)
        else:
            clusters.extend(init_conv)

    if os.path.isfile(mtx_dir + 'zeros.txt'):
        with open(mtx_dir + 'zeros.txt', 'r') as zeros:
            init = [[int(y.rstrip())] for y in zeros]
            if master_conv:
                conv_clus = [[mast_conv[y[0]]] for y in init]
                clusters.extend(conv_clus)
            else:
                clusters.extend(init)

    clusIndices = set()
    with gzip.open(out_dir + 'mcl.res.gz', 'wt') as out:
        for i, clus in enumerate(clusters):
            for hit in clus:
                out.write(str(i) + '\t' + str(hit) + '\n')
                clusIndices.add(int(hit))

    missing, count = set(range(clusLen)).difference(clusIndices), len(clusters)
    with gzip.open(out_dir + 'mcl.res.gz', 'at') as out:
        for miss in missing:
            out.write(str(count) + '\t' + str(miss) + '\n')
            count += 1
    

    with tarfile.open(mtx_dir[:-1] + '.tar.gz', 'w:gz') as tar:
        tar.add(mtx_dir, arcname = os.path.basename(mtx_dir[:-1]))
    shutil.rmtree(mtx_dir)

    return tuple([tuple(x) for x in clusters])


def prep4subgraph(mcxdump, file_in, file_out, output = subprocess.DEVNULL):
    return subprocess.call([
        mcxdump, '-imx', file_in, 
        '--dump-vlines', '-o', file_out
        ], stdout = output,
        stderr = output
        )
       
def writeMCLformat(clusters, out_dir):

    clusters = sorted(clusters, key = lambda x: len(x), reverse = True)
    clusters = [list(x) for x in clusters]
    for v in clusters:
        v.sort()
    with open(out_dir + 'clus.mcl.txt', 'w') as out:
        out.write(
            '# cline: bigmcl\n(mclheader\nmcltype matrix\ndimensions ' + \
            str(sum([len(x) for x in clusters])) + 'x' + str(len(clusters)) + \
            '\n)\n(mclmatrix\nbegin\n'
            )
        for i, v in enumerate(clusters):
            out.write(str(i) + '       ')
            out.write(' '.join([str(x) for x in v[:10]]))
            for start in range(10, len(v), 10):
                out.write('\n         ' + ' '.join([str(x) for x in v[start:start+10]]))
            out.write(' $\n')
        out.write(')')



def main(graph_in, mcxdump, inflation, out_dir, mclOut = True, row_file = None, sym = False, cpus = 1, verbose = True):

    mtx_dir = out_dir + 'mtx/'
    if not os.path.isdir(mtx_dir):
        os.mkdir(mtx_dir)

    if verbose:
        output = None
    else:
        output = subprocess.DEVNULL

    if os.path.isfile(out_dir + 'mcl.res.gz') and mclOut:
        print('\nReloading clusters and converting to MCL format', flush = True)
        clus_dict = {}
        with gzip.open(out_dir + 'mcl.res.gz', 'rt') as raw:
            for line in raw:
                d = [int(x) for x in line.rstrip().split('\t')]
                if d[0] not in clus_dict:
                    clus_dict[d[0]] = []
                clus_dict[d[0]].append(d[1])
        clusters = []
        for i in clus_dict:
            clusters.append(clus_dict[i])
        writeMCLformat(clusters, out_dir)
        print('\nComplete\n', flush = True)
        sys.exit(0)

    print('\nI. Outputting parseable rows', flush = True)
    if not row_file:
        row_file = mtx_dir + 'rows.txt'
        prep4subgraph(mcxdump, graph_in, row_file, output)

    print('\tAcquiring number of inputs', flush = True)
    in_len = runWC(row_file)
    if os.path.isfile(mtx_dir + 'complete.txt'):
        in_len += runWC(mtx_dir + 'complete.txt')
    print('\t' + str(in_len), flush = True)
    
    print('\nII. Subgraphing and MCL', flush = True)
    if cpus > 1:
        clusteringMngr(
            in_len, row_file, mtx_dir, inflation, 
            cpus = cpus, sym = sym, output = output
            )
    else:
        clusteringMngrSingle(in_len, row_file, mtx_dir, inflation, sym = sym, output = output)

    print('\nIII. Parsing clusters', flush = True)
    clusters = readSubclusters(mtx_dir, out_dir, in_len)

    if mclOut:
        writeMCLformat(clusters, out_dir)
#    with open(out_dir + 'clusters.pickle', 'wb') as out:
 #       pickle.dump(clusters)

    return out_dir + 'clus.mcl.txt'


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = \
        "Isolates disconnected graphs and runs MCL on the subgraphs. Input data must be numerical."
        )
    parser.add_argument('-i', '--input', help = 'MCL graph file in imx format', required = True)
    parser.add_argument('-I', '--inflation', required = True)
    parser.add_argument('-s', '--symmetric',
        help = 'Matrix is symmetric (throughput increase)', action = 'store_true')
    parser.add_argument('-r', '--row_file', help = 'Continue from finished row.txt')
    parser.add_argument('-m', '--mcl_format', action = 'store_true', help = 'Output clusters in MCL format')
    parser.add_argument('-o', '--output', help = 'Alternative output directory')
    parser.add_argument('-c', '--cores', default = 1, type = int)
    parser.add_argument('-v', '--verbose', action = 'store_true')
    args = parser.parse_args()

    deps = findExecs(['mcxdump', 'wc'], exit = {'mcxdump', 'wc'})
    mcxdump = deps[0]

    start_time = intro('Bigmcl.py - an MCL subgraphing procedure', {
        'Graph file': formatPath(args.input), 'Inflation': args.inflation,
        'Symmetric': args.symmetric, 'Row file': args.row_file, 'MCL format': args.mcl_format,
        'Output': args.output, 'Cores': args.cores
        })

    if not args.output:
        date = start_time.strftime('%Y%m%d')
        output = os.getcwd() + '/' + date + '_bigmcl/'
        if not os.path.isdir(output):
            os.mkdir(output)
        output = formatPath(output)
    else:
        if not os.path.isdir(args.output):
            os.mkdir(args.output)
        output = formatPath(args.output)

    main(
        formatPath(args.input), mcxdump, args.inflation, output, args.mcl_format,
        args.row_file, args.symmetric, args.cores, args.verbose
        )
    outro(start_time)
