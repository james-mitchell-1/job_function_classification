# General packages
import pandas as pd
import numpy as np
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns

# data path
project_root = Path(__file__).resolve().parent.parent

full_data_dir = project_root / "data" / "full"
out_vis_dir = project_root / "output" / "cleaned_data"
sample_data_dir = project_root / "data" 

full_data_dir.mkdir(parents=True, exist_ok=True)
out_vis_dir.mkdir(parents=True, exist_ok=True)
full_data_dir.mkdir(parents=True, exist_ok=True)
sample_data_dir.mkdir(parents=True, exist_ok=True)

# import data
aff = pd.read_csv(full_data_dir / "job_affiliations.csv")

# Duplicates
aff = aff.drop_duplicates()

# missing values
aff = aff.replace(r"^\s*$", pd.NA, regex=True)

# fix classes

# reclassify and consolidate redundant classes
function_mapping = {
    # Education [teaching]
    'Academics (Teaching & Learning)' : 'Academics (Teaching & Learning)',
    'Academics (Teaching and Learning)' : 'Academics (Teaching & Learning)', # 
    'Academics/Curriculum Design' : 'Academics (Teaching & Learning)', #

    # student
    'Student' : 'Other', # because there are so few labeled as 'Student'

    # Education [admin]
    'School Administration/Teaching' : 'School Leadership / Administration', # consider removing because of overlap with Teaching
    'School Leadership / Administration' : 'School Leadership / Administration',

    # consulting
    'Consulting' : 'Consulting',

    # data
    'Data / Analytics / Research' : 'Data / Analytics / Research',
    'Data Analysis' : 'Data / Analytics / Research', #
    'Data Analysis/Research' : 'Data / Analytics / Research', #

    # development/grants
    'Development / Grant-making' : 'Development / Grant-making',
    'Development/Grant Making' : 'Development / Grant-making', #

    # finance
    'Finance / Budgeting / Accounting': 'Finance / Budgeting / Accounting',
    'Finance/Budgeting/Accounting' : 'Finance / Budgeting / Accounting',  #

    # management
    'General Management' : 'General Management',  

    'Operations' : 'Operations',

    'Program / Project Management' : 'Program and Project Management', #
    'Program Design/Management' : 'Program and Project Management', #
    'Program and Project Management' : 'Program and Project Management',

    # planning
    'Strategic Planning' : 'Strategy and Planning', #
    'Strategy and Planning' : 'Strategy and Planning',

    # HR
    'Human Capital' : 'Human Capital / Human Resources', #
    'Human Capital / Human Resources' : 'Human Capital / Human Resources',

    # IT
    'Information Technology' : 'Technology / Systems', #
    'Technology / Systems' : 'Technology / Systems',

    # marketing / communications / external rel
    'Marketing / Communications / External Relations' : 'Marketing / Communications / External Relations',
    'Marketing/Communications/External Relations' : 'Marketing / Communications / External Relations', #

    'Sales, Business Development, and Partnerships' : 'Marketing / Communications / External Relations', #

    # policy/advocacy
    'Policy / Advocacy' : 'Policy / Advocacy',
    'Policy/Advocacy' : 'Policy / Advocacy', #

    # legal
    'Legal Services' : 'Legal Services',

    # social work
    'Social Services / Social Work' : 'Other', # absorb into 'other' because so few 

    # other
    'Other' : 'Other' 
}
aff['function'] = aff['function'].map(function_mapping)

# visualization
function_class_dist = aff['function'].value_counts().index

plt.figure(figsize=(8, 8)) 
sns.countplot(data=aff, y='function', order=function_class_dist, color = "#26AF66")

plt.xlabel("Count", fontsize = 14)
plt.ylabel("Job Function", fontsize = 14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.savefig(
    out_vis_dir / "job_functions_clean.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

## role level Visualization
# create and apply role level class mappings
role_level_mapping = {
    'Mid-level (5-7 years)' : 'Mid-level (5-7 years)', 
    'Junior-level (0-3 years)' : 'Junior-level (0-3 years)',
    'Senior-level (10+ years)' : 'Senior-level (10+ years)', 
    'Junior to Mid-level (3-5 years)' : 'Junior to Mid-level (3-5 years)',
    'Mid to Senior-level (7-10 years)' : 'Mid to Senior-level (7-10 years)', 
    'Junior to Mid-level' : 'Junior to Mid-level (3-5 years)',
    'Mid-level' : 'Mid-level (5-7 years)',
    'Junior-level' : 'Junior-level (0-3 years)', 
    'Mid to Senior-level' : 'Mid to Senior-level (7-10 years)', 
    'Senior-level' : 'Senior-level (10+ years)',
    'Entry level (0-3 years experience)' : 'Junior-level (0-3 years)',
    'Entry-mid level (3-5 years experience)' : 'Junior to Mid-level (3-5 years)'
}

aff['role_level'] = aff['role_level'].map(role_level_mapping).astype('category')

# Role level dist
role_level_dist_order = aff['role_level'].value_counts().index

plt.figure(figsize=(8, 8)) 

sns.countplot(data=aff, y='role_level', order=role_level_dist_order, color = "#2BC573")

plt.xlabel("Count", fontsize = 10)
plt.ylabel("Role Level", fontsize = 10)
plt.title('Role Levels Consolidated')

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.savefig(
    out_vis_dir / "role_levels_clean.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

## management level
#create and management level class mappings
manage_level_maping = {
    'nan' : pd.NA,
    'Manages others - 2' : 'Manages others - 2', 
    'Manages self/projects - 1' : 'Manages self/projects - 1',
    'Manages managers - 3' : 'Manages managers - 3', 
    'Manages function(s) -  4' : 'Manages function(s) - 4',
    'Manages self/projects' : 'Manages self/projects - 1', 
    'Manages others' : 'Manages others - 2',
    'Manages organization - 6' : 'Manages organization - 6', 
    'Manages a group' : 'Manages a group - 5', 
    'Manages managers' : 'Manages managers - 3',
    'Manages function(s)' : 'Manages function(s) - 4', 
    'Manages a group - 5': 'Manages a group - 5',
    'I manage(d) others. I manage(d) one or more direct reports who each manage(d) project timelines and deliverables. (Usually manager or director level)' : 'Manages managers - 3',
    'I manage(d) myself. I manage(d) project timelines and deliverables, but I do not have direct reports. (i.e. associate, analyst, teacher, attorney)' : 'Manages self/projects - 1',
    'Manage self/projects' : 'Manages self/projects - 1', 
    'Manage others' : 'Manages others - 2', 
    'Manage function(s)' : 'Manages function(s) - 4',
    'Manage organization' : 'Manages organization - 6', 
    'Manages organization' : 'Manages organization - 6', 
    'Manage managers' : 'Manages managers - 3',
    'I manage(d) a group. I manage(d) two or more managers who lead/led at least one function area each. (i.e. COO, CIO, CFO)' : 'Manages managers - 3',
    'Manages function(s) - 4' : 'Manages function(s) - 4'
}

aff['management_level'] = aff['management_level'].map(manage_level_maping).astype('category')

# Management Level dist
manage_level_dist_order = aff['management_level'].value_counts().index

plt.figure(figsize=(8, 8)) 

sns.countplot(data=aff, y='management_level', order=manage_level_dist_order, color = "#2BC573")

plt.xlabel("Count", fontsize = 10)
plt.ylabel("Management Level", fontsize = 10)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.savefig(
    out_vis_dir / "management_levels_clean.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# fix free response
# consolidate role-title
aff['role_imputed'] = aff['role'].fillna(aff['title'])

# clean up abreviations
replacements = {
    'ceo': 'chief executive officer',
    'cfo': 'chief financial officer',
    'cto': 'chief technology officer',
    'vp' : 'vice president',
    'sr' : 'senior',
    'jr' : 'junior',
    'coo' : 'chief operating officer',
    'cio' : 'chief information officer',
    'cmo' : 'chief marketing officer',
    'chro' : 'chief human resources officer',
    'clo' : 'chief legal officer',
    'cao' : 'chief administrative officer',
    'ciso' : 'chief information security officer',
    'gc' : 'general counsel',
    'evp' : 'executive vice president',
    'svp' : 'senior vice president',
    'avp' : 'assistant vice president',
    'jvp' : 'junior vice president',
    'cob' : 'chair of the board',
    'ned' : 'non-executive director',
    'gm' : 'general manager',
    'dir' : 'director',
    'mgr' : 'manager',
    'hrd' : 'human resource director',
    'hos' : 'head of sales',
    'hom' : 'head of marketing',
    'hro' : 'human resource officer',
    'fdr' : 'founder',
    'cof' : 'co-founder',
    'v.p.' : 'vice president',
}

for old, new in replacements.items():
    aff['role_imputed'] = aff['role_imputed'].str.replace(
        rf'\b{old}\b',
        new,
        case=False,
        regex=True
    )

# save complete for classification
aff.to_csv(full_data_dir / "cleaned_job_affiliations.csv", index=False)

# save sample
aff.sample(200, random_state = 34).to_csv(sample_data_dir / 'cleaned_data_sample.csv', index=False)