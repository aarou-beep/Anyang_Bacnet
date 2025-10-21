from bacpypes.core import run, stop, deferred
from bacpypes.app import BIPSimpleApplication
from bacpypes.local.device import LocalDeviceObject
from bacpypes.pdu import Address
from bacpypes.apdu import WhoIsRequest, IAmRequest
from bacpypes.primitivedata import Unsigned
import threading


# Define local BACnet device
this_device = LocalDeviceObject(
    objectName='clientOnly',
    objectIdentifier=1000,
    maxApduLengthAccepted=1024,
    segmentationSupported='noSegmentation',
    vendorIdentifier=15,
)

# Define BACnet/IP application
app = BIPSimpleApplication(
    this_device,
    Address('192.168.1.101/24')  # local IP 
)


# Handle incoming I-Am responses
def indication(apdu):
    if isinstance(apdu, IAmRequest):
        print(f"I-AM from device {apdu.iAmDeviceIdentifier} at {apdu.pduSource}")


app.indication = indication


# Send Who-Is broadcast
def send_whois():
    print("Sending Who-Is request (broadcast)...")
    whois = WhoIsRequest()
    whois.pduDestination = Address("255.255.255.255")  
    app.request(whois)


# Auto-stop after timeout
def stop_after_delay(seconds):
    def stop_func():
        print(f"\nTimeout reached ({seconds}s). Stopping BACpypes...")
        stop()
    threading.Timer(seconds, stop_func).start()


# Run sequence
deferred(send_whois)
stop_after_delay(5)

print("Running BACpypes... waiting for I-Am responses...")
run()
print("BACpypes stopped.")
