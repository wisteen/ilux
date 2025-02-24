SOCIALS = [
    ('fa-linkedin', 'LinkedIn'),
    ('fa-github', 'GitHub'),
    ('fa-twitter', 'Twitter'),
    ('fa-facebook', 'Facebook'),
    ('fa-instagram', 'Instagram'),
    ('fa-youtube', 'YouTube'),
    ('fa-pinterest', 'Pinterest'),
    ('fa-reddit', 'Reddit'),
    ('fa-stack-overflow', 'Stack Overflow'),
    ('fa-medium', 'Medium'),
    ('fa-dribbble', 'Dribbble'),
    ('fa-behance', 'Behance'),
    ('fa-snapchat', 'Snapchat'),
    ('fa-tiktok', 'TikTok'),
    ('fa-vimeo', 'Vimeo'),
    ('fa-slack', 'Slack'),
    ('fa-telegram', 'Telegram'),
    ('fa-whatsapp', 'WhatsApp'),
    ('fa-discord', 'Discord'),
    ('fa-weixin', 'WeChat'),
    ('fa-tumblr', 'Tumblr'),
    ('fa-flickr', 'Flickr'),
    ('fa-quora', 'Quora'),
    ('fa-soundcloud', 'SoundCloud'),
    ('fa-twitch', 'Twitch'),
    ('fa-spotify', 'Spotify'),
    ('fa-gitlab', 'GitLab'),
    ('fa-bitbucket', 'Bitbucket'),
    ('fa-rss', 'RSS'),
    ('fa-stack-exchange', 'Stack Exchange'),
    ('fa-kickstarter', 'Kickstarter'),
    ('fa-product-hunt', 'Product Hunt'),
    # Add more platforms as needed
]

PROFILE_VISIBILITY_CHOICES = [
    ('public', 'Public'),
    ('private', 'Private'),
    # ('specific', 'Specific Organizations'),
]


LEVEL = [
    ('Basic', 'Basic'),
    ('Intermediate', 'Intermediate'),
    ('Expert', 'Expert'),
]

SKILL_LEVEL = [
    ('10', '1'),
    ('20', '2'),
    ('30', '3'),
    ('40', '4'),
    ('50', '5'),
    ('60', '6'),
    ('70', '7'),
    ('80', '8'),
    ('90', '9'),
    ('100', '10'),


]

DEGREE_CHOICES = [
    # High School
    ('high_school', 'High School Diploma'),
    
    # Associate Degrees
    ('associate', 'Associate Degree'),
    ('aa', 'AA (Associate of Arts)'),
    ('as', 'AS (Associate of Science)'),
    ('aas', 'AAS (Associate of Applied Science)'),
    ('aaf', 'AAF (Associate of Arts in Fine Arts)'),
    ('aad', 'AAD (Associate of Applied Design)'),
    
    # Bachelor's Degrees
    ('bachelor', "Bachelor’s Degree"),
    ('ba', 'BA (Bachelor of Arts)'),
    ('bsc', 'BSc (Bachelor of Science)'),
    ('beng', 'BEng (Bachelor of Engineering)'),
    ('bfa', 'BFA (Bachelor of Fine Arts)'),
    ('bba', 'BBA (Bachelor of Business Administration)'),
    ('bed', 'BEd (Bachelor of Education)'),
    ('bsw', 'BSW (Bachelor of Social Work)'),
    ('barch', 'BArch (Bachelor of Architecture)'),
    ('blaw', 'LLB (Bachelor of Laws)'),
    ('bcom', 'BCom (Bachelor of Commerce)'),
    ('bdes', 'BDes (Bachelor of Design)'),
    ('bpharm', 'BPharm (Bachelor of Pharmacy)'),
    ('bpsy', 'BPsy (Bachelor of Psychology)'),
    ('bsn', 'BSN (Bachelor of Science in Nursing)'),
    ('bth', 'BTh (Bachelor of Theology)'),
    ('bmus', 'BMus (Bachelor of Music)'),
    ('bvid', 'BVid (Bachelor of Videography)'),
    
    # Master's Degrees
    ('master', "Master’s Degree"),
    ('ma', 'MA (Master of Arts)'),
    ('ms', 'MS (Master of Science)'),
    ('mba', 'MBA (Master of Business Administration)'),
    ('mfa', 'MFA (Master of Fine Arts)'),
    ('meng', 'MEng (Master of Engineering)'),
    ('med', 'MEd (Master of Education)'),
    ('mpa', 'MPA (Master of Public Administration)'),
    ('mph', 'MPH (Master of Public Health)'),
    ('mpp', 'MPP (Master of Public Policy)'),
    ('mha', 'MHA (Master of Health Administration)'),
    ('macc', 'MAcc (Master of Accounting)'),
    ('mfa', 'MFA (Master of Fine Arts)'),
    ('mft', 'MFT (Master of Family Therapy)'),
    ('mscba', 'MSCBA (Master of Science in Criminal Justice)'),
    ('msw', 'MSW (Master of Social Work)'),
    ('mlitt', 'MLitt (Master of Letters)'),
    ('mres', 'MRes (Master of Research)'),
    ('mphil', 'MPhil (Master of Philosophy)'),
    ('msn', 'MSN (Master of Science in Nursing)'),
    
    # Doctoral Degrees
    ('phd', 'Ph.D. (Doctor of Philosophy)'),
    ('edd', 'EdD (Doctor of Education)'),
    ('dsc', 'DSc (Doctor of Science)'),
    ('dba', 'DBA (Doctor of Business Administration)'),
    ('dnp', 'DNP (Doctor of Nursing Practice)'),
    ('dns', 'DNS (Doctor of Nursing Science)'),
    ('dsw', 'DSW (Doctor of Social Work)'),
    ('dmd', 'DMD (Doctor of Dental Medicine)'),
    ('dds', 'DDS (Doctor of Dental Surgery)'),
    ('dvm', 'DVM (Doctor of Veterinary Medicine)'),
    ('jd', 'JD (Juris Doctor)'),
    ('llm', 'LL.M. (Master of Laws)'),
    ('pharmd', 'PharmD (Doctor of Pharmacy)'),
    ('psyd', 'PsyD (Doctor of Psychology)'),
    ('thd', 'ThD (Doctor of Theology)'),
    ('dphil', 'DPhil (Doctor of Philosophy)'),
    
    # Professional Degrees
    ('md', 'MD (Doctor of Medicine)'),
    ('jd', 'JD (Juris Doctor)'),
    ('pharmd', 'PharmD (Doctor of Pharmacy)'),
    ('psyd', 'PsyD (Doctor of Psychology)'),
    ('dmd', 'DMD (Doctor of Dental Medicine)'),
    ('dds', 'DDS (Doctor of Dental Surgery)'),
    ('dvm', 'DVM (Doctor of Veterinary Medicine)'),
    ('mba', 'MBA (Master of Business Administration)'),
    ('mfa', 'MFA (Master of Fine Arts)'),
    ('llb', 'LLB (Bachelor of Laws)'),
    ('llm', 'LL.M. (Master of Laws)'),
    
    # Other Degrees
    ('other', 'Other'),
    # Add more degree types as needed
]



ALL_SKILLS = [
    ('python', 'Python'),
    ('java', 'Java'),
    ('c++', 'C++'),
    ('c#', 'C#'),
    ('javascript', 'JavaScript'),
    ('typescript', 'TypeScript'),
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('sql', 'SQL'),
    ('ruby', 'Ruby'),
    ('php', 'PHP'),
    ('swift', 'Swift'),
    ('kotlin', 'Kotlin'),
    ('go', 'Go'),
    ('rust', 'Rust'),
    ('scala', 'Scala'),
    ('perl', 'Perl'),
    ('bash', 'Bash/Shell'),
    ('r', 'R'),
    ('matlab', 'MATLAB'),
    ('dart', 'Dart'),
    ('objective_c', 'Objective-C'),
    ('vb_net', 'VB.NET'),
    ('assembly', 'Assembly'),
    ('lua', 'Lua'),
    ('elixir', 'Elixir'),
    ('clojure', 'Clojure'),
    ('haskell', 'Haskell'),
    ('cobol', 'COBOL'),
    ('fortran', 'Fortran'),
    ('groovy', 'Groovy'),
    ('visual_basic', 'Visual Basic'),
    ('powershell', 'PowerShell'),
    ('sas', 'SAS'),
    ('stata', 'Stata'),
    ('sp_ssas', 'SPSS'),
    ('mongodb', 'MongoDB'),
    ('postgresql', 'PostgreSQL'),
    ('mysql', 'MySQL'),
    ('sqlite', 'SQLite'),
    ('redis', 'Redis'),
    ('cassandra', 'Cassandra'),
    ('couchdb', 'CouchDB'),
    ('firebase', 'Firebase'),
    ('oracle', 'Oracle'),
    ('sql_server', 'SQL Server'),
    ('hadoop', 'Hadoop'),
    ('spark', 'Apache Spark'),
    ('kafka', 'Apache Kafka'),
    ('docker', 'Docker'),
    ('kubernetes', 'Kubernetes'),
    ('aws', 'Amazon Web Services (AWS)'),
    ('azure', 'Microsoft Azure'),
    ('gcp', 'Google Cloud Platform'),
    ('terraform', 'Terraform'),
    ('ansible', 'Ansible'),
    ('chef', 'Chef'),
    ('puppet', 'Puppet'),
    ('jenkins', 'Jenkins'),
    ('git', 'Git'),
    ('svn', 'Subversion (SVN)'),
    ('mercurial', 'Mercurial'),
    ('gitlab', 'GitLab'),
    ('bitbucket', 'Bitbucket'),
    ('jira', 'Jira'),
    ('confluence', 'Confluence'),
    ('slack', 'Slack'),
    ('microsoft_teams', 'Microsoft Teams'),
    ('zoom', 'Zoom'),
    ('salesforce', 'Salesforce'),
    ('sap', 'SAP'),
    ('azure_devops', 'Azure DevOps'),
    ('bitbucket_pipelines', 'Bitbucket Pipelines'),
    ('circleci', 'CircleCI'),
    ('travis_ci', 'Travis CI'),
    ('webpack', 'Webpack'),
    ('babel', 'Babel'),
    ('gulp', 'Gulp'),
    ('grunt', 'Grunt'),
    ('react', 'React'),
    ('angular', 'Angular'),
    ('vue_js', 'Vue.js'),
    ('svelte', 'Svelte'),
    ('ember', 'Ember.js'),
    ('backbone', 'Backbone.js'),
    ('django', 'Django'),
    ('flask', 'Flask'),
    ('rails', 'Ruby on Rails'),
    ('laravel', 'Laravel'),
    ('spring', 'Spring Framework'),
    ('express', 'Express.js'),
    ('nodejs', 'Node.js'),
    ('nestjs', 'NestJS'),
    ('asp_net', 'ASP.NET'),
    ('graphql', 'GraphQL'),
    ('rest_api', 'REST API'),
    ('soap_api', 'SOAP API'),
    ('swagger', 'Swagger'),
    ('openapi', 'OpenAPI'),
    ('tensorflow', 'TensorFlow'),
    ('keras', 'Keras'),
    ('pytorch', 'PyTorch'),
    ('scikit_learn', 'Scikit-learn'),
    ('pandas', 'Pandas'),
    ('numpy', 'NumPy'),
    ('matplotlib', 'Matplotlib'),
    ('seaborn', 'Seaborn'),
    ('tableau', 'Tableau'),
    ('power_bi', 'Power BI'),
    ('excel', 'Microsoft Excel'),
    ('access', 'Microsoft Access'),
    ('vba', 'VBA (Visual Basic for Applications)'),
    ('autocad', 'AutoCAD'),
    ('solidworks', 'SolidWorks'),
    ('blender', 'Blender'),
    ('maya', 'Maya'),
    ('unreal_engine', 'Unreal Engine'),
    ('unity', 'Unity'),
    ('arduino', 'Arduino'),
    ('raspberry_pi', 'Raspberry Pi'),
    ('iot', 'IoT (Internet of Things)'),
    ('blockchain', 'Blockchain'),
    ('ethereum', 'Ethereum'),
    ('solidity', 'Solidity'),
    ('bitcoin', 'Bitcoin'),
    ('cryptography', 'Cryptography'),
    ('machine_learning', 'Machine Learning'),
    ('data_science', 'Data Science'),
    ('big_data', 'Big Data'),
    ('data_analysis', 'Data Analysis'),
    ('data_visualization', 'Data Visualization'),
    ('cybersecurity', 'Cybersecurity'),
    ('penetration_testing', 'Penetration Testing'),
    ('ethical_hacking', 'Ethical Hacking'),
    ('networking', 'Networking'),
    ('information_security', 'Information Security'),
    ('system_administration', 'System Administration'),
    ('cloud_computing', 'Cloud Computing'),
    ('devops', 'DevOps'),
    ('agile', 'Agile Methodologies'),
    ('scrum', 'Scrum'),
    ('kanban', 'Kanban'),
    ('version_control', 'Version Control'),
    ('ci_cd', 'CI/CD'),
    ('api_development', 'API Development'),
    ('microservices', 'Microservices'),
    ('serverless', 'Serverless Architecture'),
    ('mobile_development', 'Mobile Development'),
    ('android', 'Android Development'),
    ('ios', 'iOS Development'),
    ('cross_platform', 'Cross-Platform Development'),
    ('front_end', 'Front-End Development'),
    ('back_end', 'Back-End Development'),
    ('full_stack', 'Full-Stack Development'),
    ('ui_ux_design', 'UI/UX Design'),
    ('graphic_design', 'Graphic Design'),
    ('seo', 'SEO (Search Engine Optimization)'),
    ('content_management', 'Content Management'),
    # Add more technical skills as needed

    ('communication', 'Communication'),
    ('teamwork', 'Teamwork'),
    ('problem_solving', 'Problem Solving'),
    ('adaptability', 'Adaptability'),
    ('critical_thinking', 'Critical Thinking'),
    ('time_management', 'Time Management'),
    ('leadership', 'Leadership'),
    ('work_ethic', 'Work Ethic'),
    ('creativity', 'Creativity'),
    ('conflict_resolution', 'Conflict Resolution'),
    ('decision_making', 'Decision Making'),
    ('empathy', 'Empathy'),
    ('positivity', 'Positivity'),
    ('active_listening', 'Active Listening'),
    ('stress_management', 'Stress Management'),
    ('public_speaking', 'Public Speaking'),
    ('negotiation', 'Negotiation'),
    ('attention_to_detail', 'Attention to Detail'),
    ('organizational_skills', 'Organizational Skills'),
    ('interpersonal_skills', 'Interpersonal Skills'),
    ('flexibility', 'Flexibility'),
    ('responsibility', 'Responsibility'),
    ('initiative', 'Initiative'),
    ('motivation', 'Motivation'),
    ('collaboration', 'Collaboration'),
    ('adaptability_to_change', 'Adaptability to Change'),
    ('self_motivation', 'Self-Motivation'),
    ('active_learning', 'Active Learning'),
    ('customer_service', 'Customer Service'),
    ('patience', 'Patience'),
    ('reliability', 'Reliability'),
    ('positive_attitude', 'Positive Attitude'),
    ('goal_setting', 'Goal Setting'),
    ('strategic_planning', 'Strategic Planning'),
    ('conflict_management', 'Conflict Management'),
    ('multitasking', 'Multitasking'),
    ('team_building', 'Team Building'),
    ('cultural_awareness', 'Cultural Awareness'),
    ('self_awareness', 'Self-Awareness'),
    ('persuasion', 'Persuasion'),
    ('emotional_intelligence', 'Emotional Intelligence'),
    ('resourcefulness', 'Resourcefulness'),
    ('decision_quality', 'Decision Quality'),
    ('public_relations', 'Public Relations'),
    ('team_leadership', 'Team Leadership'),
    ('dependability', 'Dependability'),
    ('mentoring', 'Mentoring'),
    ('coaching', 'Coaching'),
    ('trustworthiness', 'Trustworthiness'),
    ('open_mindedness', 'Open-Mindedness'),
    ('detail_oriented', 'Detail Oriented'),
    ('ability_to_learn', 'Ability to Learn'),
    ('self_discipline', 'Self-Discipline'),
    ('problem_analysis', 'Problem Analysis'),
    ('active_collaboration', 'Active Collaboration'),
    ('critical_analysis', 'Critical Analysis'),
    ('conflict_resolution_skills', 'Conflict Resolution Skills'),
    ('lead_by_example', 'Lead by Example'),
    ('ethical_judgment', 'Ethical Judgment'),
    ('trust_building', 'Trust Building'),
    ('responsibility_sharing', 'Responsibility Sharing'),
    ('conflict_handling', 'Conflict Handling'),
    ('collaborative_work', 'Collaborative Work'),
    ('problem_resolution', 'Problem Resolution'),
    ('strategic_decision_making', 'Strategic Decision Making'),
    ('team_orientation', 'Team Orientation'),
    ('adaptability_trait', 'Adaptability Trait'),
    ('leadership_skill', 'Leadership Skill'),
    ('time_effectiveness', 'Time Effectiveness'),
    ('creative_innovation', 'Creative Innovation'),
    ('self_reliance', 'Self-Reliance'),
    ('flexible_attitude', 'Flexible Attitude'),
    ('team_cooperation', 'Team Cooperation'),
    ('self_initiative', 'Self Initiative'),
    ('conflict_negotiation', 'Conflict Negotiation'),
    ('positive_outlook', 'Positive Outlook'),
    ('effective_communication', 'Effective Communication'),
    ('time_organization', 'Time Organization'),
    ('strategic_thinking', 'Strategic Thinking'),
    ('problem_identification', 'Problem Identification'),
    ('active_engagement', 'Active Engagement'),
    ('creative_thinking', 'Creative Thinking'),
    ('flexible_mindset', 'Flexible Mindset'),
    ('leadership_qualities', 'Leadership Qualities'),
    ('effective_listening', 'Effective Listening'),
    ('self_management', 'Self Management'),
    ('creative_problem_solving', 'Creative Problem Solving'),
    ('team_player', 'Team Player'),
    ('influence', 'Influence'),
    ('persuasive_communication', 'Persuasive Communication'),
    ('constructive_feedback', 'Constructive Feedback'),
    ('self_confidence', 'Self Confidence'),
    ('interpersonal_relationships', 'Interpersonal Relationships'),
    ('motivational_skills', 'Motivational Skills'),
    ('time_organization_skills', 'Time Organization Skills'),
    ('emotional_regulation', 'Emotional Regulation'),
    ('active_participation', 'Active Participation'),
    ('adaptation_skills', 'Adaptation Skills'),
    ('analytical_thinking', 'Analytical Thinking'),
    ('decision_making_skills', 'Decision Making Skills'),
    ('effective_listening', 'Effective Listening'),
    ('conflict_management_skills', 'Conflict Management Skills'),
    ('positive_mindset', 'Positive Mindset'),
    ('collaborative_spirit', 'Collaborative Spirit'),
    ('problem_solving_skills', 'Problem Solving Skills'),
    ('self_reliance', 'Self-Reliance'),
    ('active_learning', 'Active Learning'),
    ('constructive_feedback', 'Constructive Feedback'),
    # Add more soft skills as needed
]


ACTIVITY_TYPE_CHOICES = [
    ('club', 'Club/Organization'),
    ('volunteering', 'Volunteering'),
    ('competition', 'Competition'),
    ('leadership', 'Leadership Role'),
    ('other', 'Other'),
]


GOAL_TYPE_CHOICES = [
    ('short_term', 'Short-Term'),
    ('long_term', 'Long-Term'),
]


SCHOLARSHIP_PREFERENCE_CHOICES = [
    ('merit_based', 'Merit-Based'),
    ('need_based', 'Need-Based'),
    ('stemm', 'STEM-Focused'),
    ('other', 'Other'),
]


LETTER_TYPE_CHOICES = [
    ('academic', 'Academic'),
    ('professional', 'Professional'),
]


PROFESSION = [
    ('accountant', 'Accountant'),
    ('actor', 'Actor'),
    ('actuary', 'Actuary'),
    ('administrator', 'Administrator'),
    ('advertising_manager', 'Advertising Manager'),
    ('aerospace_engineer', 'Aerospace Engineer'),
    ('agricultural_engineer', 'Agricultural Engineer'),
    ('air_traffic_controller', 'Air Traffic Controller'),
    ('architect', 'Architect'),
    ('archaeologist', 'Archaeologist'),
    ('art_director', 'Art Director'),
    ('artist', 'Artist'),
    ('astronomer', 'Astronomer'),
    ('athlete', 'Athlete'),
    ('attorney', 'Attorney'),
    ('auditor', 'Auditor'),
    ('baker', 'Baker'),
    ('banker', 'Banker'),
    ('biologist', 'Biologist'),
    ('biomedical_engineer', 'Biomedical Engineer'),
    ('bookkeeper', 'Bookkeeper'),
    ('botanist', 'Botanist'),
    ('business_analyst', 'Business Analyst'),
    ('carpenter', 'Carpenter'),
    ('cashier', 'Cashier'),
    ('chef', 'Chef'),
    ('chemical_engineer', 'Chemical Engineer'),
    ('chemist', 'Chemist'),
    ('civil_engineer', 'Civil Engineer'),
    ('clergy', 'Clergy'),
    ('coach', 'Coach'),
    ('computer_programmer', 'Computer Programmer'),
    ('construction_manager', 'Construction Manager'),
    ('consultant', 'Consultant'),
    ('copywriter', 'Copywriter'),
    ('customer_service_representative', 'Customer Service Representative'),
    ('dancer', 'Dancer'),
    ('data_analyst', 'Data Analyst'),
    ('database_administrator', 'Database Administrator'),
    ('dentist', 'Dentist'),
    ('designer', 'Designer'),
    ('detective', 'Detective'),
    ('dietitian', 'Dietitian'),
    ('doctor', 'Doctor'),
    ('economist', 'Economist'),
    ('editor', 'Editor'),
    ('electrical_engineer', 'Electrical Engineer'),
    ('electrician', 'Electrician'),
    ('emergency_medical_technician', 'Emergency Medical Technician'),
    ('engineer', 'Engineer'),
    ('entrepreneur', 'Entrepreneur'),
    ('environmental_engineer', 'Environmental Engineer'),
    ('event_planner', 'Event Planner'),
    ('fashion_designer', 'Fashion Designer'),
    ('film_director', 'Film Director'),
    ('financial_advisor', 'Financial Advisor'),
    ('firefighter', 'Firefighter'),
    ('fitness_trainer', 'Fitness Trainer'),
    ('florist', 'Florist'),
    ('food_scientist', 'Food Scientist'),
    ('forensic_scientist', 'Forensic Scientist'),
    ('game_designer', 'Game Designer'),
    ('graphic_designer', 'Graphic Designer'),
    ('hair_stylist', 'Hair Stylist'),
    ('healthcare_administrator', 'Healthcare Administrator'),
    ('historian', 'Historian'),
    ('hotel_manager', 'Hotel Manager'),
    ('human_resources_manager', 'Human Resources Manager'),
    ('illustrator', 'Illustrator'),
    ('industrial_designer', 'Industrial Designer'),
    ('industrial_engineer', 'Industrial Engineer'),
    ('information_technology_specialist', 'Information Technology Specialist'),
    ('interior_designer', 'Interior Designer'),
    ('investment_banker', 'Investment Banker'),
    ('journalist', 'Journalist'),
    ('judge', 'Judge'),
    ('landscape_architect', 'Landscape Architect'),
    ('lawyer', 'Lawyer'),
    ('librarian', 'Librarian'),
    ('logistics_manager', 'Logistics Manager'),
    ('machine_learning_engineer', 'Machine Learning Engineer'),
    ('marketing_manager', 'Marketing Manager'),
    ('mechanical_engineer', 'Mechanical Engineer'),
    ('meteorologist', 'Meteorologist'),
    ('microbiologist', 'Microbiologist'),
    ('musician', 'Musician'),
    ('nurse', 'Nurse'),
    ('nutritionist', 'Nutritionist'),
    ('occupational_therapist', 'Occupational Therapist'),
    ('optometrist', 'Optometrist'),
    ('painter', 'Painter'),
    ('paramedic', 'Paramedic'),
    ('paralegal', 'Paralegal'),
    ('pharmacist', 'Pharmacist'),
    ('photographer', 'Photographer'),
    ('physical_therapist', 'Physical Therapist'),
    ('physician', 'Physician'),
    ('physician_assistant', 'Physician Assistant'),
    ('pilot', 'Pilot'),
    ('plumber', 'Plumber'),
    ('police_officer', 'Police Officer'),
    ('politician', 'Politician'),
    ('professor', 'Professor'),
    ('programmer', 'Programmer'),
    ('project_manager', 'Project Manager'),
    ('psychologist', 'Psychologist'),
    ('public_relations_specialist', 'Public Relations Specialist'),
    ('quality_assurance_specialist', 'Quality Assurance Specialist'),
    ('radiologist', 'Radiologist'),
    ('real_estate_agent', 'Real Estate Agent'),
    ('receptionist', 'Receptionist'),
    ('recruiter', 'Recruiter'),
    ('researcher', 'Researcher'),
    ('restaurant_manager', 'Restaurant Manager'),
    ('retail_manager', 'Retail Manager'),
    ('robotics_engineer', 'Robotics Engineer'),
    ('sales_manager', 'Sales Manager'),
    ('sculptor', 'Sculptor'),
    ('social_worker', 'Social Worker'),
    ('software_developer', 'Software Developer'),
    ('software_engineer', 'Software Engineer'),
    ('solicitor', 'Solicitor'),
    ('statistician', 'Statistician'),
    ('surgeon', 'Surgeon'),
    ('teacher', 'Teacher'),
    ('technical_writer', 'Technical Writer'),
    ('translator', 'Translator'),
    ('transportation_planner', 'Transportation Planner'),
    ('urban_planner', 'Urban Planner'),
    ('veterinarian', 'Veterinarian'),
    ('video_editor', 'Video Editor'),
    ('web_developer', 'Web Developer'),
    ('writer', 'Writer'),
    ('yoga_instructor', 'Yoga Instructor'),
    ('zoologist', 'Zoologist'),
    ('advertising_copywriter', 'Advertising Copywriter'),
    ('art_therapist', 'Art Therapist'),
    ('automotive_engineer', 'Automotive Engineer'),
    ('aviation_inspector', 'Aviation Inspector'),
    ('biochemist', 'Biochemist'),
    ('cartographer', 'Cartographer'),
    ('chemical_technician', 'Chemical Technician'),
    ('chiropractor', 'Chiropractor'),
    ('clinical_laboratory_technologist', 'Clinical Laboratory Technologist'),
    ('compliance_officer', 'Compliance Officer'),
    ('construction_worker', 'Construction Worker'),
    ('credit_analyst', 'Credit Analyst'),
    ('dermatologist', 'Dermatologist'),
    ('dispatcher', 'Dispatcher'),
    ('drone_pilot', 'Drone Pilot'),
    ('elevator_installer', 'Elevator Installer'),
    ('emergency_dispatcher', 'Emergency Dispatcher'),
    ('energy_auditor', 'Energy Auditor'),
    ('environmental_scientist', 'Environmental Scientist'),
    ('fashion_buyer', 'Fashion Buyer'),
    ('flight_attendant', 'Flight Attendant'),
    ('forensic_psychologist', 'Forensic Psychologist'),
    ('geneticist', 'Geneticist'),
    ('geologist', 'Geologist'),
    ('home_health_aide', 'Home Health Aide'),
    ('immigration_officer', 'Immigration Officer'),
    ('industrial_hygienist', 'Industrial Hygienist'),
    ('insurance_agent', 'Insurance Agent'),
    ('interpreter', 'Interpreter'),
    ('investment_analyst', 'Investment Analyst'),
    ('jeweler', 'Jeweler'),
    ('kinesiologist', 'Kinesiologist'),
    ('locksmith', 'Locksmith'),
    ('marine_biologist', 'Marine Biologist'),
    ('massage_therapist', 'Massage Therapist'),
    ('mechanic', 'Mechanic'),
    ('medical_lab_technician', 'Medical Lab Technician'),
    ('midwife', 'Midwife'),
    ('mortician', 'Mortician'),
    ('network_administrator', 'Network Administrator'),
    ('nuclear_engineer', 'Nuclear Engineer'),
    ('nursing_assistant', 'Nursing Assistant'),
    ('occupational_health_safety_specialist', 'Occupational Health and Safety Specialist'),
    ('paleontologist', 'Paleontologist'),
    ('personal_trainer', 'Personal Trainer'),
    ('philosopher', 'Philosopher'),
    ('podiatrist', 'Podiatrist'),
    ('psychiatrist', 'Psychiatrist'),
    ('public_health_specialist', 'Public Health Specialist'),
    ('radiation_therapist', 'Radiation Therapist'),
    ('recreational_therapist', 'Recreational Therapist'),
    ('risk_manager', 'Risk Manager'),
    ('school_principal', 'School Principal'),
    ('sound_engineer', 'Sound Engineer'),
    ('speech_language_pathologist', 'Speech Language Pathologist'),
    ('substance_abuse_counselor', 'Substance Abuse Counselor'),
    ('surgical_technologist', 'Surgical Technologist'),
    ('tax_advisor', 'Tax Advisor'),
    ('tutor', 'Tutor'),
    ('veterinary_technician', 'Veterinary Technician'),
    ('wind_turbine_technician', 'Wind Turbine Technician'),
    ('warehouse_manager', 'Warehouse Manager'),
    ('watchmaker', 'Watchmaker'),
    ('web_designer', 'Web Designer'),
    ('wedding_planner', 'Wedding Planner'),
    ('welder', 'Welder'),
    ('wind_farm_manager', 'Wind Farm Manager'),
    ('winemaker', 'Winemaker'),
    ('woodworker', 'Woodworker'),
    ('writer_technical', 'Technical Writer'),
    ('yacht_captain', 'Yacht Captain'),
    ('yoga_therapist', 'Yoga Therapist'),
    ('youth_counselor', 'Youth Counselor'),
    ('zoning_inspector', 'Zoning Inspector'),
    ('zookeeper', 'Zookeeper'),
    ('zoologist_researcher', 'Zoologist Researcher'),
    ('water_resource_specialist', 'Water Resource Specialist'),
    ('wildlife_biologist', 'Wildlife Biologist'),
    ('wind_energy_engineer', 'Wind Energy Engineer'),
    ('wood_machine_operator', 'Wood Machine Operator'),
    ('writer_script', 'Scriptwriter'),
    ('writer_speech', 'Speechwriter'),
    ('x_ray_technician', 'X-Ray Technician'),
    ('youth_pastor', 'Youth Pastor'),
    ('waste_management_specialist', 'Waste Management Specialist'),
    ('water_treatment_operator', 'Water Treatment Operator'),
    ('watch_repairer', 'Watch Repairer'),
    ('web_editor', 'Web Editor'),
    ('window_cleaner', 'Window Cleaner'),
    ('wine_taster', 'Wine Taster'),
    ('wool_sorter', 'Wool Sorter'),
    ('wood_carver', 'Wood Carver'),
    ('writer_novelist', 'Novelist'),
    ('writer_poet', 'Poet'),
    ('yoga_teacher', 'Yoga Teacher'),
    ('youth_worker', 'Youth Worker'),
    ('zinc_plater', 'Zinc Plater'),
    ('zumba_instructor', 'Zumba Instructor'),
    ('water_quality_scientist', 'Water Quality Scientist'),
    ('wedding_photographer', 'Wedding Photographer'),
    ('wildlife_conservationist', 'Wildlife Conservationist'),
    ('wind_power_technician', 'Wind Power Technician'),
    ('wood_finisher', 'Wood Finisher'),
    ('workplace_health_safety_officer', 'Workplace Health & Safety Officer'),
    ('x_ray_engineer', 'X-Ray Engineer'),
    ('yacht_designer', 'Yacht Designer'),
    ('yarn_spinner', 'Yarn Spinner'),
    ('yoga_practitioner', 'Yoga Practitioner'),
    ('youth_development_specialist', 'Youth Development Specialist'),
    ('zamboni_driver', 'Zamboni Driver'),
    ('zoo_veterinarian', 'Zoo Veterinarian'),
    ('zoonotic_disease_specialist', 'Zoonotic Disease Specialist'),
    ('zoological_park_manager', 'Zoological Park Manager')
]
