<?php
// MySQL məlumatlarına qoşulmaq
$conn = new mysqli("localhost", "root", "root", "student_db");

if ($conn->connect_error) {
    die("Bağlantı səhvi: " . $conn->connect_error);
}

// Axtarış sorğusu
$search = '';
if (isset($_POST['search'])) {
    $search = $_POST['search'];
}

// Sorğu
$sql = "SELECT * FROM students WHERE name LIKE '%$search%'";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tələbə Cədvəli</title>
    <style>
        /* Ümumi bədən stili */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: #333;
        }

        /* Ana konteyner */
        .container {
            max-width: 1200px;
            margin: 50px auto;
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #2575fc;
        }

        /* Axtarış formu */
        form {
            text-align: center;
            margin-bottom: 30px;
        }

        input[type="text"] {
            width: 300px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        input[type="text"]:focus {
            outline: none;
            border-color: #2575fc;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        input[type="submit"] {
            padding: 10px 20px;
            background-color: #2575fc;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: #1e60c8;
        }

        /* Cədvəl tərtibatı */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        table, th, td {
            border: 1px solid #ddd;
        }

        th, td {
            padding: 12px;
            text-align: left;
        }

        th {
            background-color: #2575fc;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        tr:hover {
            background-color: #f1f1f1;
        }

        /* Media sorğuları */
        @media (max-width: 768px) {
            input[type="text"] {
                width: 80%;
            }

            input[type="submit"] {
                width: 80%;
                padding: 12px;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Tələbə Cədvəli</h2>

    <!-- Axtarış Formu -->
    <form method="POST" action="">
        <input type="text" name="search" placeholder="Tələbənin adını axtar" value="<?php echo $search; ?>">
        <input type="submit" value="Axtar">
    </form>

    <!-- Tələbələrin məlumatlarının göstərilməsi -->
    <table>
        <tr>
            <th>ID</th>
            <th>Adı</th>
            <th>Yaşı</th>
            <th>Universitet</th>
            <th>Bal</th>
        </tr>
        <?php
        if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                echo "<tr>
                        <td>{$row['id']}</td>
                        <td>{$row['name']}</td>
                        <td>{$row['age']}</td>
                        <td>{$row['university']}</td>
                        <td>{$row['score']}</td>
                      </tr>";
            }
        } else {
            echo "<tr><td colspan='5'>Məlumat tapılmadı</td></tr>";
        }
        ?>
    </table>
</div>

</body>
</html>

<?php
$conn->close();
?>
