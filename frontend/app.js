async function uploadFiles() {
    const input = document.getElementById('pdfs');
    const files = input.files;
    const formData = new FormData();

    for (let i = 0; i < files.length; i++) {
        formData.append('pdfs', files[i]);
    }

    const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    console.log(result);

    if (response.status === 200) {
        alert('Files uploaded successfully');
    } else {
        alert('Error uploading files: ' + result.error);
    }
}
