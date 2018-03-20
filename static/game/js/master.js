function slugify(text) {
    return text.toString().toLowerCase()
        .replace(/\s+/g, '-')           // Replace spaces with -
        .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
        .replace(/\-\-+/g, '-')         // Replace multiple - with single -
        .replace(/^-+/, '')             // Trim - from start of text
        .replace(/-+$/, '');            // Trim - from end of text
};

function levelup_char(char_id) {
    axios.get('/game/'+char_id+'/levelup')
        .then(function (response) {
            alert(response.data.message);
            location.reload();
        })
        .catch(function (error) {
            console.log(error);
        })
};

function applyDifference() {
    difference = document.getElementById('difference').value;
    char_name = document.getElementById('char_name').value;
    char_name = slugify(char_name);
    axios.get('/game/'+char_name+'/'+difference+'/applydifference')
        .then(function (response) {
            alert(response.data.message);
            location.reload();
        })
        .catch(function (error) {
            console.log(error);
        });
};

function giveItem() {
    item = document.getElementById('item_name').value;
    char = document.getElementById('char_name01').value;
    item_name = slugify(item);
   char_name = slugify(char);
    axios.get('/game/'+char_name+'/'+item_name+'/giveitem')
        .then(function (response) {
            alert(response.data.message);
            location.reload();
        })
        .catch(function (error) {
            console.log(error);
        });
}
