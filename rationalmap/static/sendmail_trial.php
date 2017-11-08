<?php

//Importacion de las variables del formulario de trial
@$email = $_POST["email"];
 
//Preparacion del mensaje
$header = "From: $email\n" //La persona que envia el correo
 . "Reply-To: $email\n";
$subject = "www.rationalmap.com - TRIAL REQUEST"; //asunto del correo
$email_to = "icorrreas@zentyal.com";
$content = "Se ha enviado un mensaje desde la sección TRIAL de la web www.rationalmap.com\n"
. "\n"
. "$email "
. "ha solicitado el envío de la trial"
. "\n";
 
//Enviamos el mensaje y comprobamos el resultado
if (@mail($email_to, $subject ,$content ,$header )) {
 
//Si el mensaje se envía muestra una confirmación
//die("Message sent successfully. Thank you!");
    header('Location: http://www.rationalmap.com/thanks_trial.html');
}else{
 
//Si el mensaje no se envía muestra el mensaje de error
die("Your information cannot be sent. Try it later, please.");
}

?>