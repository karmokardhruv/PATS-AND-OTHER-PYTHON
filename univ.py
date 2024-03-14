math=set( )
phy=set( )
che=set( )
cs=set( )
m_N=int(input("Enter Maths No"))
for i in range (0,m_N):
    val=input("Enter Regno")
    math=math|{val}
m_P=int(input("Enter Physics No"))
for i in range (0, m_P):
    val=input ("Enter Regno")
    phy=phy | {val}
m_C=int(input( "Enter Chemistry No") )
for i in range (0, m_C) :
    val=input ("Enter Regno")
    che=che|{val}
m_CS=int (input("Enter Computer No"))
for i in range (0,m_CS) :
    val=input("Enter Regno")
    cs=cs | {val}
failure = math | phy | che | cs
print(len(failure))