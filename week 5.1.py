'''print('-----------แนะนำตัว---------------------------')
class nisit:
        def __init__(self,name,sex,year,department,ID):
            self.name = name
            self.sex = sex
            self.year = year
            self.department = department
            self.ID =ID

        def แนะนำตัว(self) :
            print('ชื่อ-นามสกุล:   ',self.name) 
            print('เพศ: ',self.sex)
            print('ปีการศึกษา: ',self.year)
            print('สาขา: ',self.department)
            print('รหัสนักศึกษา:',self.ID)
x=nisit('ธีมากร สามเสน ','ชาย ',' ปี1',' คอม','633050338-2')
x.แนะนำตัว()'''

i=1
products =['พารารักษาใจ 30บาท','แก้หวัดตัดปัญหา 50บาท','ขนมจีนน้ำยาล้างพิษ 80บาท']
def menu():
    global choice
    print('-----------ธีมากร อาหารยา เช้า เที่ยง เย็น----------')
    print('1.แสดงรายการสินค้า [s]\n2.เพิ่มรายการสินค้า[a]\n3.ออกจากระบบ[o]\n')
    choice =input('กรุณาเลือกคำส่ั่ง: ')

def show():
    class shop:
        def __init__(shop,pro1,pro2,pro3):
            shop.pro1 = pro1
            shop.pro2 = pro2
            shop.pro3 = pro3

        def shoplist(shop) :
            print('รายการสินค้ามีดังนี้\n')
            print('1: ',shop.pro1)
            print('2: ',shop.pro2)
            print('3: ',shop.pro3)

    c=shop('พารารักษาใจ 30บาท','แก้หวัดตัดปัญหา 50บาท','ขนมจีนน้ำยาล้างพิษ 80บาท')
    c.shoplist()

def showlistupdate():
    n =str(input('สินค้าที่จะเพิ่มคือ: '))
    products.append(n)



while True:
    menu()
    if choice == 's':
        show()
    elif choice == 'a':
        showlistupdate()
    else:
        u =str(input('ต้องการออกโปรแกรมใช่หรือไม่ (y/n) :'))
        if u == "y":
            print('ออกจากโปรแกรมเรียบร้อยแล้ว')
            break
        else:
            print('กลับสู่โปรแกรม')

