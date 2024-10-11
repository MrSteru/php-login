<?php
// Отримуємо дані з форми
$username = $_POST['username'];
$password = $_POST['password'];

// Валідація - проста перевірка на наявність даних
if (!empty($username) && !empty($password)) {
    // Формат запису: username і password
    $data = "Username: " . $username . " | Password: " . $password . "\n";
    
    // Відкриваємо файл для запису, або створюємо новий, якщо його не існує
    $file = 'user_data.txt';
    
    // Записуємо дані в файл
    file_put_contents($file, $data, FILE_APPEND | LOCK_EX);
    
    // Підтверджуємо успішний запис
    echo "Login successful. Data saved!";
} else {
    echo "Please fill in both username and password.";
}
?>
