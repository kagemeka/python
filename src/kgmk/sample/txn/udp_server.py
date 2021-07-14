import time 

from kagemeka.txn import (
  UDPSvr,
  Addr,
)


class Hdlr:

  def __call__(
    self,
    *args,
    **kwargs,
  ):
    return self.handle(
      *args,
      **kwargs,
    )


  def handle(
    self,
    data,
    addr,
  ):
    print(data)
    return data




class UDPRecieve:
  def run(self):

    hdlr = Hdlr()

    addr = Addr(
      '127.0.0.1',
      8001,
    )


    svr = UDPSvr(
      addr=addr,
      hdlr=hdlr,
    )

    p = svr.create_process()
    p.start()

    time.sleep(1<<4)
    p.terminate()
    p.join()



if __name__ == '__main__':
  test = UDPRecieve()
  test.run()