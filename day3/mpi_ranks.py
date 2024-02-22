#!/usr/bin/env python3

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
a = np.array([1])
b = np.array([2])
c = np.array([3])

if rank == 0:
    print("Process", rank, "asociated with number", a)
    
if rank == 1:
    print("Process", rank, "asociated with number", b)
    
if rank == 2:
    print("Process", rank, "asociated with number", c)

# print(“hello world from process ", rank)