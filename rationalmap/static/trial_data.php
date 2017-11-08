<?php

//Importacion de las variables del formulario de contacto
@$sector = addslashes($_POST['sector']);
@$area = addslashes($_POST['area']);
@$email = 'jdgarcia@zentyal.com';

//Mensaje de contacto
$header = "From: $email\n"
. "Reply to: $email\n"; //La persona que envia el correo
$subject = "www.rationalmap.com - TRIAL REQUEST"; //asunto del correo
$email_to = "juande.garcia.kincubator@gmail.com";
$content = "Un interesado ha enviado un mensaje desde la trial de www.rationalmap.com\n"
. "\n"
. "Sector: $sector\n"
. "Area: $area\n"
. "\n";
 
//Enviamos el mensaje y comprobamos el resultado
if (mail($email_to, $subject ,$content ,$header )) {
 
//Si el mensaje se envía muestra una confirmación
//die("Message sent successfully. Thank you!");
    header('Location: ./trial_page3.html');
}else{
 
//Si el mensaje no se envía muestra el mensaje de error
die("Your information cannot be sent. Try it later, please.");
}

?>