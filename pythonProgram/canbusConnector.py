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

#print(firstID.signals)



can_bus = can.interface.Bus('can1', bustype='socketcan')

data = firstID.encode({'Engine_Speed': 250.1, 'Manifold_Pressure': 10, 'Throttle_Position': 0, 'Coolant_Pressure': 25})
data2 = secondID.encode({'Fuel_Pressure': 250.1, 'Oil_Pressure': 10, 'Engine_Demand': 0, 'Wastegate_Pressure': 25})


i = 0
while i < 6440:
    data = firstID.encode({'Engine_Speed': i, 'Manifold_Pressure': 10, 'Throttle_Position': 0, 'Coolant_Pressure': 25})
    data2 = secondID.encode({'Fuel_Pressure': 250.1, 'Oil_Pressure': i, 'Engine_Demand': 0, 'Wastegate_Pressure': 25})

    message = can.Message(arbitration_id=firstID.frame_id, data=data)
    message2 = can.Message(arbitration_id=secondID.frame_id, data=data2)

    can_bus.send(message)
    can_bus.send(message2)

    time.sleep(0.02)
    print(("Sent Data + {}").format(i))
    i += 10


can_bus.shutdown()
