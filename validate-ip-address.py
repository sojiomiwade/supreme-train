def validateIP(ip):
  """
  @param ip: str
  @return: bool
  ensure we have four tokens on a split by dot
  ensure each token is int, in between 0 and 255 inclusive
  1.2.oops.4
  1.2.-7.4
  01.2.7.4 -> false
  1...
  
exception ValueError
Raised when an operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.


  time,space: O(n)-->O(1)   ,O(n)--> O(1)  
  """
  items=ip.split('.')
  if len(items) != 4:
    return False
  for item in items:
    val=None
    try:
      val=int(item)
    except ValueError: #int('4&2') ...
      return False      
    assert val is not None
    if len(item)>1 and item[0]=='0':
      return False
    if not 0<=val<=255:
      return False
  return True