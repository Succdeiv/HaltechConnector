import cantools
import can
import pprint
import time
import os

os.system('sudo ifconfig can1 down')
os.system('sudo ip link set can1 type can bitrate 1000000')
os.system('sudo ifconfig can1 up')

dbcFile = cantools.database.load_file('Haltech-Broadcast-V2.35.0.dbc')
#print(dbcFile.messages)
#print(dbcFile.get_message_by_name('ID_0x360'))
firstID = dbcFile.get_message_by_name('ID_0x360')
secondID = dbcFile.get_message_by_name('ID_0x361')
thirdID = dbcFile.get_message_by_name('ID_0x3E0')
fourthID = dbcFile.get_message_by_name('ID_0x372')


can_bus = can.interface.Bus('can1', bustype='socketcan')
i=0
j=0
y=0
up = True
for x in range(50000):
    x += 1
    if up == True:
        i += 50
        j += 6
        y += 4
        if i > 7000:
            up = False
    if up == False:
        i -= 50
        j -= 6
        y -= 4
        if i <= 0:
            up = True

    data = firstID.encode({'Engine_Speed': i, 'Manifold_Pressure': 10, 'Throttle_Position': 0, 'Coolant_Pressure': 25})
    data2 = secondID.encode({'Fuel_Pressure': 250.1, 'Oil_Pressure': j, 'Engine_Demand': 0, 'Wastegate_Pressure': 25})
    data3 = thirdID.encode({'Coolant_Temperature': y, 'Air_Temperature': 45, 'Fuel_Temperature': 0, 'Oil_Temperature': 25})
    data4 = fourthID.encode({'Battery_Voltage': 13.3, 'Target_Boost_Level': 58, 'Barometric_Pressure': 0})


    message = can.Message(arbitration_id=firstID.frame_id, data=data)
    message2 = can.Message(arbitration_id=secondID.frame_id, data=data2)
    message3 = can.Message(arbitration_id=thirdID.frame_id, data=data3)
    message4 = can.Message(arbitration_id=fourthID.frame_id, data=data4)

    can_bus.send(message)
    can_bus.send(message2)
    can_bus.send(message3)
    can_bus.send(message4)


    time.sleep(0.5)
    print(("Sent Data + {}").format(i))

can_bus.shutdown()


