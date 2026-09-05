---
tags:
  - verification
---
This is a challenge to write a test to detect the problem in the code:
```java
class BoundedBuffer {

synchronized
void put(Object x) throws InterruptedException {
  while( occupied == buffer.length )
wait();
  notify();
  ++occupied;
  putAt %= buffer.length;
  buffer[putAt++] = x;
}

synchronized
Object take() throws InterruptedException {
  while( occupied == 0 )
wait();
  notify();
  --occupied;
  takeAt %= buffer.length;
  return buffer[takeAt++];
}

private Object[] buffer = new Object[4];
private int putAt, takeAt, occupied;
}
```