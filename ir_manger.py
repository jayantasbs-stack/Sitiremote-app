from jnius import autoclass, cast

def get_ir_manager():
    """Accesses the IR hardware safely only when called."""
    try:
        # These are inside the function to avoid the 'Terminal' error
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Context = autoclass('android.content.Context')
        activity = PythonActivity.mActivity
        
        ir_service = activity.getSystemService(Context.CONSUMER_IR_SERVICE)
        return cast('android.hardware.ConsumerIrManager', ir_service)
    except Exception as e:
        print(f"JNI Error: {e}")
        return None

def is_ir_available():
    """Checks if the device actually has an IR emitter."""
    manager = get_ir_manager()
    if manager:
        return manager.hasIrEmitter()
    return False

def transmit_code(pattern):
    """Sends the actual light pulses."""
    manager = get_ir_manager()
    if manager and manager.hasIrEmitter():
        # Standard frequency for Siti/NEC protocol is 38kHz
        manager.transmit(38000, pattern)
