from kagemeka.gen import (
  JsonDumpable as JD,
  JsonCodec as JC,
)

from kagemeka.txn import (
  UDPClient,
)


class UDPSend:
  def run(self):
    addr = ('0.0.0.0', 8001)
    data = {
      'None': None,
      'list': [1, 2, 3],
      'japanese': 'あいうえお',
    }
    with UDPClient(
      addr=addr,
    ) as svr:
      svr.send_(data)
      data = svr.receive()
    
    print(data)


if __name__ == '__main__':
  i = 0
  while True:
    test = UDPSend()
    test.run()
    print(i)
    i += 1

