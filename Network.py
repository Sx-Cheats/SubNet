
class _Error(Exception):
        def __call__(self, *args, **kwds ) :
            return self
        def __getattribute__(self, __name: str):
            return self 

def _err(e):
        try:
          raise _Error(e)
        except _Error as _e:
                return e

def iplen(func):
        def check(*args,**kwargs):
                if(args[1].__len__()!=args[2].__len__()):
                        print(_err('Error : Invalid Ip'))
                        exit()

                return func(*args,**kwargs)
        return check
class adress_operator:
        def _split_s(self,text,step):
               return [(text[x:x+step]).__str__() for x in range(0,text.__len__(),step)]  
        def _bin(self,_A):
          return ['{:08b}'.format(x) for x in _A]
        
        def _bin_to_dec(self,_bin):
                return [ int(x,2) for x in self._split_s(_bin,8)]
        def _dec(self,_A):
          return [int(x,2) for x in _A]
        def _max(self,__C,__A1):
                return self._bin_to_dec(('0'+('1'*(__C-1))+(''.join(self._bin(__A1))[::-1])[__C:])[::-1])
        @iplen
        def _sub(self,__A1, __A2):
  
                return [ __A1[x]-__A2[x] for x in range(__A1.__len__())]
        @iplen
        def _and(self,__A1,__A2):
                return [ __A1[x]&__A2[x] for x in range(__A1.__len__())]
    
class IPV4(object):
        def __init__(self,ip,mask) -> None:  
           self.__ip = ip
           self.__AO=adress_operator()
           self.CAPACITY_OUTPUT = 2**14-2 #16382 /18
           self.__mask = mask['address']
           self.__capacity = mask['bits_capacity']
           self.__na= self.__AO._and(self.__ip,self.__mask) 
           self.__firshost = self.__na[:3] + [self.__na[3]+1]
           self.__lasthost = self.__AO._max(self.__capacity,self.__ip)
           self.__mask_generic = self.__AO._sub([255,255,255,255],self.__mask)
           self.__ip_class = 'D (Multicast)' if 239 >= self.__ip[0] >= 224 else 'A' if 127 >= self.__ip[0] >= 0 else'B' if 191 >= self.__ip[0] >= 128 else 'C' if  223 >= self.__ip[0] >= 192 else 'Ip reserved (E+)'
           
           self.INT=1
           self.BIN=9
           self.STR=3
           self.BYTES = 12
           self.HEX=18
        def __get_format__(self):
                print('___'*11,'\n')
                print('IPV4 (object).INT (CODE : 1)')
                print('___'*11,'\n')
                print('IPV4 (object).STR (CODE : 3)')
                print('___'*11,'\n')
                print('IPV4 (object).BIN (CODE : 9)')
                print('___'*11,'\n')
                print('IPV4 (object).BYTES (CODE : 12)')
                print('___'*11,'\n')
                print('IPV4 (object).HEX (CODE : 18)')
                print('___'*18,'\n')
                print('IPV4 (object).STR | IPV4  (object).HEX (CODE : 19)')
                print('___'*18,'\n')
                print('IPV4 (object).STR | IPV4  (object).BIN (CODE : 11)')
                print('___'*18,'\n')
        def __repr__(self) -> str:
            return ("Subnet Calculator | By: $x-Cheats#9633")

        def __format_adress(self,format,adress):
                if(format==3):
                  return '.'.join(map(str,adress))
                elif (format==1):
                    return adress
                elif(format == 9):
                        return self.__AO._bin(adress)
                elif(format==11):
                        return '.'.join(self.__AO._bin(adress))
                elif(format==12):
                        return bytes(bytearray(adress)) 
                elif(format==18):
                        return [*map(lambda a: '0x{:1x}'.format(a),adress)]
                elif(format==19):
                        return '.'.join([*map(lambda a: '0x{:1x}'.format(a),adress)])
                else:
                  return -1
        def ip_class(self):
                return self.__ip_class
        def generic_mask(self,format=1):
                return self.__format_adress(format,self.__mask_generic) 
        def mask_capacity(self):
                return self.__capacity
        def Broadcast(self,format=1):
                return self.__format_adress(format,self.__lasthost[:3]+[self.__lasthost[3]+1]) 

        def total_hosts(self):
          return 2**self.__capacity

        def usable_hosts(self):
           return 2**self.__capacity-2
        def firsthost(self,format=1):
                return self.__format_adress(format,self.__firshost) 
        
        def lasthost(self,format=1):
                return self.__format_adress(format,self.__lasthost) 

        def ip_adress(self,format=1):
                 return self.__format_adress(format,self.__ip)
        def mask_adress(self,format=1):
                return self.__format_adress(format,self.__mask)
        def network_adress(self,format=1):
                return self.__format_adress(format,self.__na)

        def get_hosts(self,format=1):
                if(2**self.__capacity-2 >= self.CAPACITY_OUTPUT):
                        res = input('Are you sure to output all hosts (Y/Yes/Yeah) ? :')
                        if(res.lower() != 'y' and res.lower()!='yes' and res.lower()!='yeah'):
                                del res
                                return -1

                __subip = ''.join(self.__AO._bin(self.__firshost))[::-1][self.__capacity::][::-1]
                return [self.__format_adress(format,self.__AO._bin_to_dec(__subip+('{:b}'.format(x)).rjust(self.__capacity,'0'))) for x in range(1,2**self.__capacity-1)]            

        def output_data(self):
                print('___'*11,'\n')
                print("Ip address = ", self.ip_adress(self.STR),'\n')
                print("Mask = ",self.mask_adress(self.STR))
                print('___'*11,'\n')
                print("Network address = ",self.network_adress(self.STR))
                print('___'*11,'\n')
                print('Mask bits capacity = ',self.mask_capacity())
                print('___'*11,'\n')
                print("Total Host = ",self.total_hosts())
                print("Usable Host = ",self.usable_hosts())
                print('___'*11,'\n')
                print("First host address =",self.firsthost(self.STR))
                print("Last host address =",self.lasthost(self.STR))
                print('___'*11,'\n')
                print('Broadcast address = ',self.Broadcast(self.STR))
                print('___'*11,'\n')
                print('Generic mask = ',self.generic_mask(self.STR))
                print('___'*11,'\n')
                print('Ip class = ',self.ip_class()) 
                print('___'*11,'\n')
                print('Range of address usable = \n\t', '\n\t'.join(self.get_hosts(self.STR)))
                print('___'*11,'\n')


class Network:
        
   def __init__(self) -> None:
     self.mask = self.__g_mn()
     self._ip=-1
     self._mask=-1
   def mask_network(self):
            return self.mask 

   def network(self,ip:str=-1) -> IPV4:
        try:
                if(type(ip)!=str):
                        raise 
                ip = ip.split('/')
                assert ip.__len__() ==2
                self._ip =  [*map(int,ip[0].split('.'))]
                assert self._ip.__len__() ==4
                if(not '.' in ip[1]):
                   self._mask = self.mask['/'+ip[1]]
                elif '.' in ip[1]:
                        __ = [*map(int,ip[1].split('.'))]
                        for x in enumerate(self.mask):    
                                if (__==self.mask[x[1]]['address']):
                                      self._mask=self.mask[x[1]]
                                      del __,self.mask
                                      break
                                elif (x[0]==self.mask.__len__()-1):
                                        raise 
                del ip                                     
        except Exception:
                return _err('Error : Invalid Ip')
             
               
        return IPV4(self._ip,self._mask)
   def __g_mn(self):
        A,R,O,Mask = [0,0,0,0],0,1.28e2,{}
        for x in range(1,33):
                A[R]+=int(O)
                Mask['/'+x.__str__()] =  {"bits_capacity":32-x, "address":A[:]}
                O /=2 
                if(not ((x+8)%8)):     
                        A[R]=255
                        O= 1.28e2
                        R+= 1
        del A,R,O
        return Mask
       


