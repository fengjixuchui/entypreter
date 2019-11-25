DESCRIPTION = "Display all stagers or all implants."

def autocomplete(shell, line, text, state):
    pass

def help(shell):
    shell.print_plain("")
    shell.print_plain('Use "modules -s" to display all available stagers.')
    shell.print_plain('Use "modules -i" to display all available implants.')
    shell.print_plain("")

def execute(shell, cmd):

    splitted = cmd.split()

    if len(splitted) > 1:
        flag = splitted[1]
        if flag == "-s":
            print("")
            print("        NAME         DESCRIPTION")                
            print("        ----         -----------")                
            print("        mshta        Serves payloads using MSHTA.exe HTML Applications (default).")
            print("        regsvr       Serves payloads using regsvr32.exe COM+ scriptlets.")
            print("        wmic         Serves payloads using WMIC XSL.")
            print("        rundll32_js  Serves payloads using rundll32.exe.")
            print("        disk         Serves payloads using files on disk.")
            print("        bitsadmin    Transfers a .wsf payload containing JScript over a Bitsadmin job and executes it.")
            print("")
                
        elif flag == "-i":
            print("")
            print("        NAME                        DESCRIPTION")                
            print("        ----                        -----------")
            print("        bypassuac_compdefaults      Bypass UAC via registry hijack for ComputerDefaults.exe.")
            print("        bypassuac_compmgmtlauncher  Bypass UAC via registry hijack for CompMgmtLauncher.exe.")
            print("        bypassuac_eventvwr          Uses eventvwr.exe exploit to bypass UAC on Windows 7, 8, and 10.")
            print("        bypassuac_fodhelper         Bypass UAC via registry hijack for fodhelper.exe.")
            print("        bypassuac_sdclt             Uses sdclt.exe exploit to bypass UAC on Windows 10.")
            print("        bypassuac_slui              Bypass UAC via registry hijack for slui.exe.")
            print("        system_createservice        Elevate from administrative session to SYSTEM via SC.exe.")
            print("        youtube                     Maxes volume and opens the specified YouTube video in a hidden window.")
            print("        voice                       Plays a message over text-to-speech.")
            print("        clipboard                   Retrieves the current content of the user clipboard.")
            print("        comsvcs_lsass               Utilizes comsvcs.dll to create a MiniDump of LSASS, parses with pypykatz.")
            print("        enum_domain_info            Retrieve information about the Windows domain.")
            print("        hashdump_dc                 Domain controller hashes from the NTDS.dit file.")
            print("        hashdump_sam                Retrieves hashed passwords from the SAM hive.")
            print("        loot_finder                 Finds loot on the target box.")
            print("        user_hunter                 Locate users logged on to domain computers (using Dynamic Wrapper X).")
            print("        mimikatz_dotnet2js          Injects a reflective-loaded DLL to run powerkatz.dll.")
            print("        mimikatz_dynwrapx           Injects a reflective-loaded DLL to run powerkatz.dll (using Dynamic Wrapper X).")
            print("        mimikatz_tashlib            Executes arbitrary shellcode using the TashLib COM object.")
            print("        shellcode_dotnet2js         Executes arbitrary shellcode using the DotNet2JS technique.")
            print("        shellcode_dynwrapx          Executes arbitrary shellcode using the Dynamic Wrapper X COM object.")
            print("        shellcode_excel             Runs arbitrary shellcode payload (if Excel is installed).")
            print("        enable_rdesktop             Enables remote desktop on the target.")
            print("        exec_cmd                    Run an arbitrary command on the target, and optionally receive the output.")
            print("        add_user                    Adds a either a local or domain user.")
            print("        registry                    Adds a Proton stager payload in the registry.")
            print("        schtasks                    Establishes persistence via a scheduled task.")
            print("        wmi                         Creates persistence using a WMI subscription.")
            print("        password_box                Prompt a user to enter their password.")
            print("        exec_psexec                 Run a command on another machine using psexec from sysinternals.")
            print("        exec_wmi                    Executes a command on another system.")
            print("        stage_wmi                   Hook a zombie on another machine using WMI.")
            print("        tcp                         Uses HTTP to scan open TCP ports on the target zombie LAN.")
            print("        download_file               Downloads a file from the target zombie.")
            print("        multi_module                Run a number of implants in succession.")
            print("        upload_file                 Uploads a file from the listening server to the target zombies.")
            print("")
    else:
        help(shell)
