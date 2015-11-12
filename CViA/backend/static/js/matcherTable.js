$(document).ready( function () {
    var url = window.location.href;
    var job_id = url.split("/");
    if(job_id[job_id.length-1].length > 0){
        job_id = job_id[job_id.length-1].toString();
    }
    else {
        job_id = job_id[job_id.length-2].toString();
    }
    renderTable("#cv_list", job_id); 
});

function renderTable(target, job_id) {
    var table = $(target).DataTable({
        'ajax': { 
            'url': '../../get_matching_cvs/'+job_id+'/',
            'dataSrc': processData,
            'order': [[ 0, "desc" ]] // Order by the first column (score)
        },
        'deferRender': true,
        'columns': [
            {'data': 'score.total', 'title': 'Total Score'},
            {'data': 'resume.name', 'title': 'Name'},
            {'data': 'resume.education', 'title': 'Education'},
            {'data': 'resume.skills', 'title': 'Skills'},
            {'data': 'resume.experience', 'title': 'Experience'},
            {'data': 'resume.languages', 'title': 'Languages'},
        ]
    });
    table.order([0, 'desc']);
}

function processData(json){
    var len = json.length;
    for(var i=0; i < len; i++){    
        json[i].DT_RowId = json[i].pk;
    }
    return json;
}

