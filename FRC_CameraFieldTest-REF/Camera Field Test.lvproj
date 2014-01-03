<?xml version='1.0'?>
<Project Type="Project" LVVersion="8508002">
   <Property Name="NI.Project.Description" Type="Str"></Property>
   <Item Name="My Computer" Type="My Computer">
      <Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
      <Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
      <Property Name="server.tcp.enabled" Type="Bool">false</Property>
      <Property Name="server.tcp.port" Type="Int">0</Property>
      <Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
      <Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
      <Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
      <Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
      <Property Name="specify.custom.address" Type="Bool">false</Property>
      <Item Name="Camera Field Test.vi" Type="VI" URL="Camera Field Test.vi"/>
      <Item Name="Dependencies" Type="Dependencies">
         <Item Name="vi.lib" Type="Folder">
            <Item Name="NI_FPGA_Interface.lvlib" Type="Library" URL="/&lt;vilib&gt;/Robotics Library/NIFPGAInterface/NI_FPGA_Interface.lvlib"/>
            <Item Name="Camera.lvlib" Type="Library" URL="/&lt;vilib&gt;/Robotics Library/WPI/Camera/Camera.lvlib"/>
            <Item Name="MiniMergeError.vi" Type="VI" URL="/&lt;vilib&gt;/Robotics Library/NIFPGAInterface/ErrorManagement/MiniMergeError.vi"/>
            <Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
            <Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
            <Item Name="StatusErrorCache.ctl" Type="VI" URL="/&lt;vilib&gt;/Robotics Library/WPI/DriverStation/StatusErrorCache.ctl"/>
            <Item Name="DriverStation.lvlib" Type="Library" URL="/&lt;vilib&gt;/Robotics Library/WPI/DriverStation/DriverStation.lvlib"/>
            <Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
            <Item Name="TCP Listen.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen.vi"/>
            <Item Name="Internecine Avoider.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/Internecine Avoider.vi"/>
            <Item Name="TCP Listen Internal List.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen Internal List.vi"/>
            <Item Name="TCP Listen List Operations.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen List Operations.ctl"/>
            <Item Name="Servo.lvlib" Type="Library" URL="/&lt;vilib&gt;/Robotics Library/WPI/PWM/Servo/Servo.lvlib"/>
            <Item Name="IMAQ Create" Type="VI" URL="/&lt;vilib&gt;/Vision/Basics.llb/IMAQ Create"/>
            <Item Name="IMAQ Image.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Image.ctl"/>
            <Item Name="Image Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Type"/>
            <Item Name="nirio_resource_hc.ctl" Type="VI" URL="/&lt;vilib&gt;/userDefined/High Color/nirio_resource_hc.ctl"/>
            <Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
            <Item Name="Merge Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Merge Errors.vi"/>
            <Item Name="VariantType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/VariantDataType/VariantType.lvlib"/>
            <Item Name="PID Control Input Filter.vi" Type="VI" URL="/&lt;vilib&gt;/addons/control/pid/pid.llb/PID Control Input Filter.vi"/>
            <Item Name="PID Control Input Filter (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/addons/control/pid/pid.llb/PID Control Input Filter (DBL).vi"/>
            <Item Name="PID Control Input Filter (DBL Array).vi" Type="VI" URL="/&lt;vilib&gt;/addons/control/pid/pid.llb/PID Control Input Filter (DBL Array).vi"/>
            <Item Name="PWM.lvlib" Type="Library" URL="/&lt;vilib&gt;/Robotics Library/WPI/PWM/PWM.lvlib"/>
            <Item Name="DigitalModule.lvlib" Type="Library" URL="/&lt;vilib&gt;/Robotics Library/WPI/DigitalModule/DigitalModule.lvlib"/>
            <Item Name="IMAQ Extract" Type="VI" URL="/&lt;vilib&gt;/vision/Image Manipulation.llb/IMAQ Extract"/>
            <Item Name="IMAQ Cast Image" Type="VI" URL="/&lt;vilib&gt;/Vision/Management.llb/IMAQ Cast Image"/>
            <Item Name="IMAQ ColorThreshold" Type="VI" URL="/&lt;vilib&gt;/Vision/Color Processing.llb/IMAQ ColorThreshold"/>
            <Item Name="Particle Parameters" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Particle Parameters"/>
            <Item Name="IMAQ Particle Analysis" Type="VI" URL="/&lt;vilib&gt;/Vision/Analysis.llb/IMAQ Particle Analysis"/>
            <Item Name="IMAQ Or" Type="VI" URL="/&lt;vilib&gt;/Vision/Operator.llb/IMAQ Or"/>
            <Item Name="IMAQ ImageToImage 2" Type="VI" URL="/&lt;vilib&gt;/Vision/Management.llb/IMAQ ImageToImage 2"/>
            <Item Name="Dflt Data Dir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Dflt Data Dir.vi"/>
            <Item Name="IMAQ Write File 2" Type="VI" URL="/&lt;vilib&gt;/Vision/Files.llb/IMAQ Write File 2"/>
            <Item Name="IMAQ Write BMP File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write BMP File 2"/>
            <Item Name="IMAQ Write Image And Vision Info File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write Image And Vision Info File 2"/>
            <Item Name="IMAQ Write JPEG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG File 2"/>
            <Item Name="IMAQ Write JPEG2000 File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG2000 File 2"/>
            <Item Name="IMAQ Write PNG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write PNG File 2"/>
            <Item Name="IMAQ Write TIFF File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write TIFF File 2"/>
         </Item>
         <Item Name="Control States.ctl" Type="VI" URL="Control States.ctl"/>
         <Item Name="FPS Calculator.vi" Type="VI" URL="FPS Calculator.vi"/>
         <Item Name="FindTwoColor.vi" Type="VI" URL="FindTwoColor.vi"/>
         <Item Name="CreateImages.vi" Type="VI" URL="CreateImages.vi"/>
         <Item Name="SizeOrderedMorphology.vi" Type="VI" URL="SizeOrderedMorphology.vi"/>
         <Item Name="Team Designation.ctl" Type="VI" URL="Team Designation.ctl"/>
         <Item Name="Green Rects.vi" Type="VI" URL="Green Rects.vi"/>
         <Item Name="Test Second Color.vi" Type="VI" URL="Test Second Color.vi"/>
         <Item Name="Compare Sizes.vi" Type="VI" URL="Compare Sizes.vi"/>
         <Item Name="Merge Rects Vertically.vi" Type="VI" URL="Merge Rects Vertically.vi"/>
         <Item Name="Split FF Info.vi" Type="VI" URL="Split FF Info.vi"/>
         <Item Name="Single Target Info.ctl" Type="VI" URL="Single Target Info.ctl"/>
         <Item Name="BiColor Mask.vi" Type="VI" URL="BiColor Mask.vi"/>
         <Item Name="Servo Tracking State Machine.vi" Type="VI" URL="Servo Tracking State Machine.vi"/>
         <Item Name="Center of Rect.vi" Type="VI" URL="Center of Rect.vi"/>
         <Item Name="Deadband.vi" Type="VI" URL="Deadband.vi"/>
         <Item Name="nivissvc.dll" Type="Document" URL="nivissvc.dll"/>
         <Item Name="nivision.dll" Type="Document" URL="nivision.dll"/>
         <Item Name="NiRioSrv.dll" Type="Document" URL="NiRioSrv.dll"/>
      </Item>
      <Item Name="Build Specifications" Type="Build"/>
   </Item>
   <Item Name="cRIO Controller" Type="RT CompactRIO">
      <Property Name="alias.name" Type="Str">cRIO Controller</Property>
      <Property Name="alias.value" Type="Str">10.0.0.2</Property>
      <Property Name="CCSymbols" Type="Str">TARGET_TYPE,RT;OS,VxWorks;CPU,PowerPC;</Property>
      <Property Name="crio.family" Type="Str">901x</Property>
      <Property Name="host.ResponsivenessCheckEnabled" Type="Bool">true</Property>
      <Property Name="host.ResponsivenessCheckPingDelay" Type="UInt">5000</Property>
      <Property Name="host.ResponsivenessCheckPingTimeout" Type="UInt">1000</Property>
      <Property Name="host.TargetCPUID" Type="UInt">2</Property>
      <Property Name="host.TargetOSID" Type="UInt">14</Property>
      <Property Name="target.cleanupVisa" Type="Bool">false</Property>
      <Property Name="target.FPProtocolGlobals_ControlTimeLimit" Type="Int">300</Property>
      <Property Name="target.getDefault-&gt;WebServer.Port" Type="Int">80</Property>
      <Property Name="target.getDefault-&gt;WebServer.Timeout" Type="Int">60</Property>
      <Property Name="target.IsRemotePanelSupported" Type="Bool">true</Property>
      <Property Name="target.RTTarget.ApplicationPath" Type="Path">/c/ni-rt/startup/startup.rtexe</Property>
      <Property Name="target.RTTarget.EnableFileSharing" Type="Bool">true</Property>
      <Property Name="target.RTTarget.IPAccess" Type="Str">+*</Property>
      <Property Name="target.RTTarget.LaunchAppAtBoot" Type="Bool">false</Property>
      <Property Name="target.RTTarget.VIPath" Type="Path">/c/ni-rt/startup</Property>
      <Property Name="target.server.app.propertiesEnabled" Type="Bool">true</Property>
      <Property Name="target.server.control.propertiesEnabled" Type="Bool">true</Property>
      <Property Name="target.server.tcp.access" Type="Str">+*</Property>
      <Property Name="target.server.tcp.enabled" Type="Bool">true</Property>
      <Property Name="target.server.tcp.paranoid" Type="Bool">true</Property>
      <Property Name="target.server.tcp.port" Type="Int">3363</Property>
      <Property Name="target.server.tcp.serviceName" Type="Str"></Property>
      <Property Name="target.server.tcp.serviceName.default" Type="Str">Main Application Instance/VI Server</Property>
      <Property Name="target.server.vi.access" Type="Str">+*</Property>
      <Property Name="target.server.vi.callsEnabled" Type="Bool">true</Property>
      <Property Name="target.server.vi.propertiesEnabled" Type="Bool">true</Property>
      <Property Name="target.WebServer.Enabled" Type="Bool">false</Property>
      <Property Name="target.WebServer.LogEnabled" Type="Bool">false</Property>
      <Property Name="target.WebServer.LogPath" Type="Path">/c/ni-rt/system/www/www.log</Property>
      <Property Name="target.WebServer.Port" Type="Int">80</Property>
      <Property Name="target.WebServer.RootPath" Type="Path">/c/ni-rt/system/www</Property>
      <Property Name="target.WebServer.TcpAccess" Type="Str">c+*</Property>
      <Property Name="target.WebServer.Timeout" Type="Int">60</Property>
      <Property Name="target.WebServer.ViAccess" Type="Str">+*</Property>
      <Item Name="Calibrate White Balance.vi" Type="VI" URL="Calibrate White Balance.vi"/>
      <Item Name="Dependencies" Type="Dependencies">
         <Item Name="vi.lib" Type="Folder">
            <Item Name="NI_FPGA_Interface.lvlib" Type="Library" URL="/&lt;vilib&gt;/Robotics Library/NIFPGAInterface/NI_FPGA_Interface.lvlib"/>
            <Item Name="Camera.lvlib" Type="Library" URL="/&lt;vilib&gt;/Robotics Library/WPI/Camera/Camera.lvlib"/>
            <Item Name="DriverStation.lvlib" Type="Library" URL="/&lt;vilib&gt;/Robotics Library/WPI/DriverStation/DriverStation.lvlib"/>
            <Item Name="StatusErrorCache.ctl" Type="VI" URL="/&lt;vilib&gt;/Robotics Library/WPI/DriverStation/StatusErrorCache.ctl"/>
            <Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
            <Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
            <Item Name="MiniMergeError.vi" Type="VI" URL="/&lt;vilib&gt;/Robotics Library/NIFPGAInterface/ErrorManagement/MiniMergeError.vi"/>
            <Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
            <Item Name="TCP Listen.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen.vi"/>
            <Item Name="Internecine Avoider.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/Internecine Avoider.vi"/>
            <Item Name="TCP Listen List Operations.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen List Operations.ctl"/>
            <Item Name="TCP Listen Internal List.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen Internal List.vi"/>
            <Item Name="IMAQ Create" Type="VI" URL="/&lt;vilib&gt;/Vision/Basics.llb/IMAQ Create"/>
            <Item Name="IMAQ Image.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Image.ctl"/>
            <Item Name="Image Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Type"/>
         </Item>
         <Item Name="nivissvc.dll" Type="Document" URL="nivissvc.dll"/>
      </Item>
      <Item Name="Build Specifications" Type="Build"/>
   </Item>
</Project>
