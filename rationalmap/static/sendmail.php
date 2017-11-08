<?php
//Importamos las variables del formulario de contacto
@$nombre = addslashes($_POST['name']);
@$email = addslashes($_POST['email']);
@$phone = addslashes($_POST['phone']);
@$company = addslashes($_POST['company']);
@$message = addslashes($_POST['message']);
 
//Preparamos el mensaje de contacto
$header = "From: $email\n" //La persona que envia el correo
 . "Reply-To: $email\n";
$subject = "Mensaje desde la pagina web"; //asunto aparecera en la bandeja del servidor de correo
$email_to = "info@rationalmap.com"; //cambiar por tu email
$content = "$name ha enviado un mensaje desde la web www.rationalmap.com\n"
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
    header('Location: http://rationalmap2.kincubator.es');
}else{
 
//Si el mensaje no se envía muestra el mensaje de error
die("Your information cannot be sent. Try it later, please.");
}
?>