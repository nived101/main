from django.shortcuts import render
from django.templatetags.static import static  # Import static

def home(request):
    nav_items = [
    {"title": "The Institute", "submenu": [
        {"title": "About the Institute", "url": "/institute/about"},
        {"title": "Campus and Facilities", "url": "/institute/campus"},
        {"title": "Rules and Regulations", "url": "/institute/rules"},
        {"title": "RTI", "url": "/institute/rti"},
        {"title": "CVC", "url": "/institute/administration/vigilanceOfficer"},
        {"title": "Public Grievances", "url": "/PublicGrievances"},
        {"title": "Photo Gallery", "url": "/institute/gallery"},
        {"title": "Forms to Download", "url": "/forms/institute"},
        {"title": "Contact Administration", "url": "/institute/contact"},
        {"title": "NIRF", "url": "/institute/nirf"},
        {"title": "Women Cell", "url": "/womencell"},
        {"title": "ICC", "url": "/institute/ICC"},
        {"title": "Spicmacay", "url": "/institute/Spicmacay"},
        {"title": "IQAC", "url": "/institute/iqac"},
        {"title": "Newsletter (Pariprashna)", "url": "/newsletter"},
        {"title": "Campus Connect Newsletter", "url": "/campusconnect"},
        {"title": "Bulletin Ph.D Newsletter", "url": "/bulletin"},
        {"title": "Networks & Systems", "url": "/institute/netandsys"},
    ]},
    
    {"title": "Academics", "submenu": [
        {"title": "Departments", "url": "/academics/departments"},
        {"title": "Academic Office", "url": "/academics/office"},
        {"title": "Admission", "url": "/students/admission"},
        {"title": "Exam Results", "url": "/academics/results"},
        {"title": "Academic Calendar", "url": "/academics/calendar"},
        {"title": "Curriculum and Syllabi", "url": "/academics/curriculum"},
        {"title": "Institute Fee Structure", "url": "/academics/fee-structure"},
        {"title": "NEP-2020 Cell", "url": "/academics/nep"},
        {"title": "Forms to Download", "url": "/forms/academics"},
        {"title": "Rules and Regulations", "url": "/academics/rules"},
        {"title": "Convocation", "url": "/academics/convocation"},
        {"title": "NAD", "url": "/academics/nad"},
        {"title": "Scholarship", "url": "/academics/Scholarship"},
        {"title": "Exam Schedule", "url": "/academics/exam"},
        {"title": "Physical Education", "url": "/academics/physicalEducation"},
        {"title": "Emails for Contacts", "url": "/academics/emailContacts"},
        {"title": "Educational Verification Procedure", "url": "assets/pdf/Educational Verification Procedure/Procedure_for_verification2022.pdf"},
    ]},

    {"title": "Administration", "submenu": [
        {"title": "Director's Office", "url": "/institute/administration"},
    ]},

    {"title": "Students Welfare", "submenu": [
        {"title": "Rules and Regulations", "url": "/students/rulesandregulation"},
        {"title": "Anti-ragging", "url": "/students/antiragging"},
        {"title": "Student Council", "url": "/students/council"},
        {"title": "Annual Fest", "url": "/students/annualFest"},
        {"title": "Orientation", "url": "/students/orientation"},
        {"title": "Student Clubs", "url": "/students/clubs"},
        {"title": "Student Associations", "url": "/students/student-associations"},
        {"title": "Counselling Services", "url": "/students/councelling"},
        {"title": "Medical Insurance", "url": "/students/medical-insurance"},
        {"title": "NCC", "url": "/students/studentActivities/NCC"},
        {"title": "NSS", "url": "/students/studentActivities/NSS"},
        {"title": "Physical Education & Sports", "url": "/academics/physicalEducation"},
        {"title": "Forms to Download", "url": "/forms/students"},
        {"title": "Alumni Relations", "url": "/alumni/alumniRelations"},
        {"title": "Grievance Redressal", "url": "/students/Grievance Redressal"},
        {"title": "Announcements", "url": "/students/sw-announcements"},
    ]},

    {"title": "Hostel", "submenu": [
        {"title": "Hostel Administration", "url": "/hostelAdministration"},
        {"title": "Hostel Facilities", "url": "/hostel_facilities"},
        {"title": "Rules and Regulations", "url": "/assets/docs/hostel/Hostel Rules.pdf"},
        {"title": "Code of Conduct", "url": "/assets/docs/hostel/Updated code of conduct - Hostel.pdf"},
        {"title": "Circular", "url": "/circular_hostel"},
        {"title": "Contact Us", "url": "/students/hostels"},
        {"title": "Forms to Download", "url": "/forms/students"},
    ]},

    {"title": "Faculty & Staff", "submenu": [
        {"title": "Administration Head Directory", "url": "/faculty/adminDirectory"},
        {"title": "Dean Directory", "url": "/faculty/deanDirectory"},
        {"title": "HOD Directory", "url": "/faculty/hodDirectory"},
        {"title": "Faculty Directory", "url": "/faculty/facultyDirectory"},
        {"title": "Faculty On Contract Directory", "url": "/faculty/focDirectory"},
        {"title": "Officer Directory", "url": "/faculty/OfficerDirectory"},
        {"title": "P&D Directory", "url": "/faculty/P&dDirectory"},
        {"title": "Staff Directory", "url": "/faculty/staffDirectory"},
        {"title": "Career", "url": "/Opportunities"},
        {"title": "Forms to Download", "url": "/forms/faculty"},
    ]},

    {"title": "Research & Consultancy", "submenu": [
        {"title": "Research & Consultancy Office", "url": "/research/office"},
        {"title": "IEEE", "url": "/research/IEEE"},
        {"title": "List of R&C Committees", "url": "/research/committees"},
        {"title": "Patents", "url": "/research/publications"},
        {"title": "Funded Projects", "url": "/research/fundedProjects"},
        {"title": "Journals", "url": "/research/journal"},
        {"title": "Book Chapter", "url": "/research/bookChapter"},
        {"title": "Conference", "url": "/research/conference"},
        {"title": "Consultancy Projects", "url": "/research/consultancyProjects"},
        {"title": "IPR Cell", "url": "/research/ipr"},
        {"title": "Forms to Download", "url": "/forms/research"},
        {"title": "IIC", "url": "/research/innovation"},
        {"title": "NISP", "url": "/research/nisp"},
        {"title": "Industry Consultancy", "url": "/alumni/industryConsultancy"},
        {"title": "MoU", "url": "/alumni/mou"},
        {"title": "Central Instrumentation Facility (CIF)", "url": "/CIF"},
    ]},

    {"title": "Training & Placement", "submenu": [
        {"title": "About", "url": "/trainingAndPlacement"},
        {"title": "Placement Procedure", "url": "/procedure"},
        {"title": "Training Programs & Activities", "url": "/activities"},
        {"title": "Infrastructure and Facilities", "url": "/InfrastructureFacilities"},
        {"title": "Placement Statistics", "url": "/recruitments"},
        {"title": "Testimonial", "url": "/testimonial"},
        {"title": "Internship", "url": "/students/internship"},
        {"title": "Contact", "url": "/tnpcontact"},
    ]}
    ]

    instituteCarouselSlides = [
        {"link": "images/instituteCarousel/NIRF.jpg", "alt": "Slide 1"},
        {"link": "images/instituteCarousel/Banner 1.jpg", "alt": "Slide 2"},
        {"link": "images/instituteCarousel/img104.jpg", "alt": "Slide 3"},
        {"link": "images/instituteCarousel/img102.jpg", "alt": "Slide 4"},
        {"link": "images/instituteCarousel/img014.jpg", "alt": "Slide 5"},
        {"link": "images/instituteCarousel/img016.jpg", "alt": "Slide 6"},
        {"link": "images/instituteCarousel/Banner 2.jpg", "alt": "Slide 7"},
        {"link": "images/instituteCarousel/img003.jpg", "alt": "Slide 8"},
        {"link": "images/instituteCarousel/img011.jpg", "alt": "Slide 9"},
        {"link": "images/instituteCarousel/img012.jpg", "alt": "Slide 10"},
    ]

    overlayCards = [
        {"title": "Admission", "link": "/students/admission", "content": "", "new": True},
        {"title": "Directory", "link": "/people_nit", "content": ""},
        {"title": "Opportunities", "link": "/Opportunities", "content": "", "new": True},
        {"title": "Departments", "link": "/academics/departments", "content": ""}
    ]

    galleryImages = [
        {"link": "images/slideshow/img008.jpg", "alt": "Slide 8"},
        {"link": "images/slideshow/img009.jpg", "alt": "Slide 9"},
        {"link": "images/slideshow/img010.jpg", "alt": "Slide 10"},
        {"link": "images/slideshow/img011.jpg", "alt": "Slide 11"},
        {"link": "images/slideshow/img012.jpg", "alt": "Slide 12"},
    ]
    stats = [
        {"title": "10", "subtitle": "Departments"},
        {"title": "1421", "subtitle": "Students"},
        {"title": "63", "subtitle": "Faculties"},
        {"title": "1730", "subtitle": "Publications"},
    ]
    quickLinks = [
        {"title": "Gallery", "link": "/institute/gallery"},
        {"title": "Forms for Download", "link": "/forms"},
        {"title": "People at NITPY", "link": "/people_nit"},
        {"title": "NAD", "link": "/academics/nad"},
        {"title": "Women Cell", "link": "/womencell"},
        {"title": "Stores and Purchase", "link": "/institute/administration/stores"},
        {"title": "ID Cards", "link": "/idcard"},
        {"title": "Alumni", "url": "https://www.nitpyalumni.com/home/index"},
        {"title": "NISP", "link": "/research/nisp"},
        {"title": "SC/ST/OBC cell", "link": "/scstobc_cell"},
        {"title": "Networks & Systems", "link": "/institute/netandsys"},
        {"title": "List of Holidays", "url": static("docs/holidays/List_of_holidays_NIT_Puducherry_2025.pdf")},
        {"title": "Public Grievances", "link": "/PublicGrievances"},
        {"title": "Medical Facilities", "link": "/students/medical"},
        {"title": "Physical Education", "link": "/academics/physicalEducation"},
        {"title": "List of committees", "link": "/institute/administration/committeeList"},
        {"title": "PARIPRASHNA", "link": "/institute/administration/newsletter"},
        {"title": "Campus Connect Newsletter", "link": "/campusconnect"},
        {"title": "NITPY BULLETIN", "link": "/institute/administration/bulletin"},
        {"title": "Central Library", "link": "/library"},
        {"title": "DASA", "url": "https://dasanit.org/dasa2021/"},
        {"title": "SMDP", "url": "https://www.nitpy.ac.in/old_website/SMDPWebsite/"},
        {"title": "Guest House", "link": "/GuestHouse"},
        {"title": "Hostel Facilities", "link": "/hostel_facilities"},
        {"title": "NCC", "link": "/students/studentActivities/NCC"},
        {"title": "Support Center", "url": "http://172.18.5.212/"},
    ]

    # Convert relative paths to Django static paths
    for slide in instituteCarouselSlides:
        slide["link"] = static(slide["link"])

    for image in galleryImages:
        image["link"] = static(image["link"])

    return render(request, "home.html", {
        "instituteCarouselSlides": instituteCarouselSlides,
        "overlayCards": overlayCards,
        "galleryImages": galleryImages,
        "nav_items": nav_items,
        "stats": stats,
        "quickLinks": quickLinks
    })

def about(request):
    return render(request, "about.html")
