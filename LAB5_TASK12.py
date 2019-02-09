class IPv4:
    def __init__(self,ip):
        self.ip_list=[]
        self.bip_list=[]
        self.mask=None
        self.bnetwork=''
        self.network_list=[]
        self.network_list=[]
        try:
            temp_list=ip.split('.')
            temp_list[3],mask=temp_list[3].split('/')[0],temp_list[3].split('/')[1]
            for val in temp_list:
                if(int(val)>254):
                    raise
                if int(mask)>30:
                    raise
        except:
            print ('Invalid input provided.Please Provide proper Ip address and mask')
        else:
            self.ip_list=temp_list
            self.mask=mask
    def getAddress(self):
        return self.ip_list


    def binaryToDecimal(binary): 
      
        binary1 = binary 
        decimal, i, n = 0, 0, 0
        while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
        return decimal
    
    def getMask(self):
        self.bnetwork=''
        self.network_list=[]
        for i in range(32):
            if i<int(self.mask):
                self.bnetwork+='1'
            else:
                self.bnetwork+='0'
        for v in range(0,32,8):
            self.network_list.append(IPv4.binaryToDecimal(int(self.bnetwork[v:v+8])))
        return self.network_list

    def getNetwork(self):
        tempr=[]
        tempmask=self.getMask()
        for i in range(4) :
            tempr.append((int(self.ip_list[i])) & (int(tempmask[i])))
        return tempr
    def __str__(self):
        return str(self.ip_list)

    def wildmask(self):
        self.bnetwork=''
        self.network_list=[]
        for i in range(32):
            if i<int(self.mask):
                self.bnetwork+='0'
            else:
                self.bnetwork+='1'
        for v in range(0,32,8):
            self.network_list.append(IPv4.binaryToDecimal(int(self.bnetwork[v:v+8])))
        return self.network_list


    def subnet_info(self):
        temp_net=self.getNetwork()
        temp=temp_net[:]
        temp_broadcast=temp_net[:]
        temp_wild=self.wildmask()
        temp_mask=self.getMask()
        temp_ip=ip.getAddress()
        temp_broadcast[3]=temp_wild[3]
        temp_hostlist=list()
        for i in range(temp_broadcast[3]):
            makeip=('%d.%d.%d.%d') %(temp[0],temp[1],temp[2],temp[3]+i)
            temp_hostlist.append(makeip)
        print('The MAsk address ::',temp_mask)
        print('The Network address ::',temp_net)
        print('The wildmask address ::',temp_wild)
        print('The Broadcast address ::',temp_broadcast)
        print('The Host addresses address ::',temp_hostlist)
        

#ip=IPv4(input('Please Enter The Ip address with mask value(xx.xx.xx.xx/xx)::'))
#ip=IPv4('10.0.1.7/26')
#print('list representing the address::',ip.getAddress())
#print('The Mask address of Ip::',ip.getMask())
#print('The Network address of Ip::',ip.getNetwork())
#print('The WildMask address of Ip::',ip.wildmask())
ip.subnet_info()
