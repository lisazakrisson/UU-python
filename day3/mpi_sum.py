#!/usr/bin/env python3

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = np.array([rank + 1])

# Allocate space for the global sum on process 0
if rank == 0:
    process_sum = np.empty(1)

# Sum data arrays across all processes
comm.Reduce(data, process_sum, op=MPI.SUM, root=0)

if rank == 0:
    print('Sum: ' + process_sum[0])