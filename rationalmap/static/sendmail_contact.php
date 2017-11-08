<?php

//Importacion de las variables del formulario de contacto
@$name = addslashes($_POST['name']);
@$email = addslashes($_POST['email']);
@$phone = addslashes($_POST['phone']);
@$company = addslashes($_POST['company']);
@$message = addslashes($_POST['message']);
 
//Mensaje de contacto
$header = "From: $email\n" //La persona que envia el correo
 . "Reply-To: $email\n";
$subject = "www.rationalmap.com - CONTACT REQUEST"; //asunto del correo
$email_to = "juande.garcia.kincubator@gmail.com";
$content = "$name ha enviado un mensaje desde la sección CONTACT de www.rationalmap.com\n"
. "\n"
. "Name: $name\n"
. "Email: $email\n"
. "Phone: $phone\n"
. "Company: $company\n"
. "Message: $message\n"
. "\n";
 
//Enviamos el mensaje y comprobamos el resultado
if (@mail($email_to, $subject ,$content ,$header )) {
 
//Si el mensaje se envía muestra una confirmación
//die("Message sent successfully. Thank you!");
    header('Location: http://www.rationalmap.com/thanks_contact.html');
}else{
 
//Si el mensaje no se envía muestra el mensaje de error
die("Your information cannot be sent. Try it later, please.");
}

?>