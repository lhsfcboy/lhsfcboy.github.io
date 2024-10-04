
# 简单示例计算

## 前言
该示例展示了如何使用 CUDA 进行简单的向量加法，包括在主机（CPU）和设备（GPU）上分配内存、在 GPU 上并行执行向量加法并验证结果。最后代码展示了 GPU 和 CPU 执行相同任务的性能对比。

## 代码说明

```cpp
int vector_size = 64000000;  // 向量的大小
int block_num = 80000;       // 启动的块数
int thread_num = 800;        // 每个块中的线程数
int *A, *B, *C;              // 主机侧指针
int *dA, *dB, *dC;           // 设备侧指针（GPU）

// 步骤 1: 在主机上分配内存（使用 malloc）
// 为主机（CPU 侧）的向量分配内存
A = (int *)malloc(sizeof(int) * vector_size);
B = (int *)malloc(sizeof(int) * vector_size);
C = (int *)malloc(sizeof(int) * vector_size);

// 初始化主机数组
for(int i = 0; i < vector_size; i++){
    A[i] = 10;  // 将 A 的所有元素设置为 10
    B[i] = 20;  // 将 B 的所有元素设置为 20
}

// 步骤 2: 在设备上分配内存（使用 cudaMalloc）
// 为设备（GPU 侧）的向量分配内存
cudaMalloc(&dA, sizeof(int) * vector_size);
cudaMalloc(&dB, sizeof(int) * vector_size);
cudaMalloc(&dC, sizeof(int) * vector_size);

// 步骤 3: 将主机数据复制到设备（使用 cudaMemcpy）
// 将数据从主机内存复制到设备内存（A 和 B 数组）
cudaMemcpy(dA, A, sizeof(int) * vector_size, cudaMemcpyHostToDevice);
cudaMemcpy(dB, B, sizeof(int) * vector_size, cudaMemcpyHostToDevice);

// 步骤 4: 启动内核
// 使用指定的网格和块大小在 GPU 上启动向量加法内核
long long gpu_start = getCurrentTime();  // 记录 GPU 开始时间
vecadd<<<block_num, thread_num>>>(dA, dB, dC);  // 在 GPU 上执行向量加法
CudaSafeCall(cudaDeviceSynchronize());  // 确保所有线程完成计算后继续
long long gpu_end = getCurrentTime();    // 记录 GPU 结束时间

// 步骤 5: 将数据从设备复制回主机（使用 cudaMemcpy）
// 将结果（C 数组）从设备内存复制回主机内存
cudaMemcpy(C, dC, sizeof(int) * vector_size, cudaMemcpyDeviceToHost);

// 步骤 6: 验证结果（可选）
// 通过比较 C 的值和主机上 A + B 的结果来验证计算结果

// 步骤 7: 清理
// 释放设备内存（GPU）
cudaFree(dA);
cudaFree(dB);
cudaFree(dC);

// CPU 版本的向量加法用于性能比较
long long cpu_start = getCurrentTime();  // 记录 CPU 开始时间
for(int i = 0; i < vector_size; i++){
    C[i] = A[i] + B[i];  // 在 CPU 上执行向量加法
}
long long cpu_end = getCurrentTime();    // 记录 CPU 结束时间

// 输出 GPU 和 CPU 执行时间
printf("gpu time: %lld usec\n", gpu_end - gpu_start);  // GPU 执行时间（微秒）
printf("cpu time: %lld usec\n", cpu_end - cpu_start);  // CPU 执行时间（微秒）

// 释放主机内存（CPU）
free(A);
free(B);
free(C);

return 0;
```
