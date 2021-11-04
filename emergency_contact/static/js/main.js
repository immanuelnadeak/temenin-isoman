$(document).ready(function () {

    $('#pilihDaerah').change(function (e) {
        e.preventDefault();

        $("#container-rumah-sakit").empty();;
        $.ajax({
            url: "daerah_json",
            dataType: 'json',
            success: function (res) {
                $.each(res, function (i, item) {
                    const daerah = $('select[id=pilihDaerah] option').filter(':selected').val()
                    if (item.fields.daerah == daerah) {
                        var option = $(`<tr onclick="telepon('${item.fields.nama}', '${item.fields.telepon}')" style="cursor: pointer" data-bs-toggle="modal" data-bs-target="#rsModal"><td>${item.fields.nama}<br><small>${item.fields.alamat}</small></td><td class="text-center">${item.fields.telepon}</td><tr>`);
                        $("#container-rumah-sakit").append(option);
                    }
                });
            }
        });
    });
});

function telepon(nama, telepon) {
    $('#rsModalLabel').text(nama);
    $('#kalimat-telepon').text(`Apakah Anda ingin terhubung langsung ke ${nama}?`);
    $('#NomorTelepon').attr('href', `tel:${telepon}`);
}