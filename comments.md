# Running time (tree.py)

The plots are of the kind n vs t, where n is the number of iterations that we
grow the tree for and t the walltime (that is, we get the time in seconds right
before we build the tree and the time just after we finish. The walltime is the
difference of these two clocks, in seconds).

Looking at the plots in [perf_plot.png](perf_plot.png) we see that the running
time (denote this by f(n), where n is the number of iterations we grow the tree
for) follows an exponential function. The lower plot shows that
it follows an exponential function f(n) = A 2^(Bn), by taking the 2-logarithm
we get log2(f(n)) = B*n + log2(A). In the plot I have imposed the best least
squares estimates which gives that (from one of my runs, your will vary due to
natural variability in running times) B is about 0.93 and log2(A) about -18.3.

This also makes perfect sense, since we are essentially building a binary tree
and so we would expect the time f(n) = O(2^n).
