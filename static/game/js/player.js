function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
};

function slugify(text) {
    return text.toString().toLowerCase()
        .replace(/\s+/g, '-')           // Replace spaces with -
        .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
        .replace(/\-\-+/g, '-')         // Replace multiple - with single -
        .replace(/^-+/, '')             // Trim - from start of text
        .replace(/-+$/, '');            // Trim - from end of text
};

function transferItem() {
    source_char = slugify(getCookie('char'))
    target_char = slugify(document.getElementById('char_name').value);
    item_name = slugify(document.getElementById('item_name').value);

    axios.get('/game/'+source_char+'/'+target_char+'/'+item_name+'/itemtransfer')
        .then(function (response) {
            alert(response.data.message);
            location.reload();
        })
        .catch(function (error) {
            console.log(error);
        });
};