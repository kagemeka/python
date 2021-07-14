from kagemeka.gen import (
  JsonDumpable as JD,
  JsonCodec as JC,
)

from kagemeka.txn import (
  # UDPClient,
  TCPClient,
)


class TCPSend:
  def run(self):
    addr = ('0.0.0.0', 8001)
    data = {
      'None': None,
      'list': [1, 2, 3],
      'japanese': 'あいうえお',
    }
    with TCPClient(
      addr=addr,
    ) as svr:
      svr.connect_()
      svr.send_(data)
      data = svr.receive()
    
    print(data)


if __name__ == '__main__':
  i = 0
  while True:
    test = TCPSend()
    test.run()
    print(i)
    i += 1

