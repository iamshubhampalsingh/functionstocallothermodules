import oneplus.connectTodevice as connect
import oneplus.setting as settings
import oneplus.settingsMenu.wifi_network.wifi as wifi
import oneplus.settingsMenu.bluetoothDeviceconnection.bluetooth as bluetooth
import oneplus.settingsMenu.display.controls as display
import oneplus.settingsMenu.soundsVibration.contorl as soundsVibration
import oneplus.settingsMenu.buttonsGestures.quickGuestures.control as quick


device=connect.getDevice()
quick.offDoubleTaptoWake(device)
wifi.connecttoWifi(device, "OnePlus Guest", "1+NeverSettle")
bluetooth.turnonNFC(device)
bluetooth.turnoffBluetooth(device)
display.onAdaptive(device)
display.sleepModeto30min(device)
display.onAmbientDisplay(device)
display.onAmbientDisplay(device)

#print(config)

#import uiautomator2 as u2
#d=u2.connect('d70359cc')
#d.press('home')
#d.open_notification()
#d(className="android.widget.FrameLayout",resourceId="com.android.settings:id/main_content",index="0").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/container_material",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/list_container",index="0").child(className="android.widget.RelativeLayout",index="0").child(className="androidx.recyclerview.widget.RecyclerView",resourceId="com.android.settings:id/recycler_view",index="0").child(className="android.widget.LinearLayout",index="1").child(className="android.widget.LinearLayout",resourceId="android:id/widget_frame",index="1").child(className="android.widget.Switch",resourceId="android:id/switch_widget",index="0").click()