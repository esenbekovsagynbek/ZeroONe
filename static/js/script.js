let courses = document.getElementById('courses');
let aboutUs = document.getElementById('about-us')
let feedbacks = document.getElementById('feedbacks')

function coursesScroll() {
    return courses.scrollIntoView({behavior: "smooth"})
}

function aboutUsScroll() {
    return aboutUs.scrollIntoView({behavior: "smooth", block: "nearest"})
}
function feedbackUsScroll() {
    return feedbacks.scrollIntoView({behavior: "smooth"})
}
