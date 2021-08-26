const dropDown = document.querySelector('.list1')
dropDown.innerHTML = ''

axios.get('http://127.0.0.1:8000/api/posts').then(res => {

    for (key of res.data) {
        dropDown.innerHTML += `
            <tr> 
                <td>${key['user']['id']}</td>          
                <td>${key['user']['name']}</td>
                <td>${key['id']}</td>
                <td>${key['title']}</td>
                <td>${key['body']}</td>
            </tr>  
          `;
    }

})
