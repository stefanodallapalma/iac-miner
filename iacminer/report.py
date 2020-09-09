"""
This module is responsible to generate html reports for the mining
"""
import statistics
from datetime import datetime

def generate_mining_report(repositories: list) -> str:
    """
    Generate an HTML report for the crawled repositories
    """
    avg_repos = len(repositories)
    avg_issues = statistics.mean([d['issues'] for d in repositories])
    avg_releases = statistics.mean([d['releases'] for d in repositories])
    avg_stars = statistics.mean([d['stars'] for d in repositories])
    avg_watchers = statistics.mean([d['watchers'] for d in repositories])

    accordion = ''
    for item in repositories:
        accordion += '{0}\n'.format(__generate_card(item))

    return """
        <!doctype html>
        <html lang="en">
            <header>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            </header>
            <body>
                <br/>
                <div class="row text-center">
                    <div class="col text-center">
                        <h2>GithubMiner Report</h2>
                        <p class="font-weight-light text-center">This report was generated on: {0} </p> <!-- Report generation date -->
                    </div>
                </div>
    
                <div class="row">   
                    <div class="col">
                        <div class="card align-items-center">
                            <br/>
                            <i class="fa fa-database fa-2x" style="color:#007bff;"></i>
                            <h2>{1}</h2>  <!-- Number of repositories -->
                            <p class="font-weight-light text-center">Repositories</p>
                        </div>
                    </div>   
                    <div class="col">
                        <div class="card align-items-center">
                            <br/> 
                            <i class="fa fa-exclamation-circle fa-2x" style="color:#dc3545;"></i>
                            <h2>{2}</h2>  <!-- Average number of issues -->
                            <p class="font-weight-light ">Avg issues</p>
                        </div>
                    </div>   
                    <div class="col">
                        <div class="card align-items-center">
                            <br/> 
                            <i class="fa fa-tag fa-2x" style="color:#28a745;"></i>
                            <h2>{3}</h2>  <!-- Average number of release -->
                            <p class="font-weight-light ">Avg releases</p>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card align-items-center">
                            <br/>
                            <i class="fa fa-star fa-2x" style="color:#ffc107;"></i>
                            <h2>{4}</h2>  <!-- Average number of stars -->
                            <p class="font-weight-light text-center">Avg stars</p>
                        </div>
                    </div>   
                    <div class="col">
                        <div class="card align-items-center">
                            <br/>
                            <i class="fa fa-eye fa-2x" style="color:#17a2b8;"></i>
                            <h2>{5}</h2>  <!-- Average number of watchers -->
                            <p class="font-weight-light text-center">Avg watchers</p>
                        </div>
                    </div>
                </div>
                <br/>
                <div class="accordion" id="accordion">
                {6}  <!-- Accordion: list of cards containing repos'information -->
                </div>
              <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
              <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
              <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
            </body>
        </html> 
        """.format(
            datetime.today(),
            avg_repos,
            avg_issues,
            avg_releases,
            avg_stars,
            avg_watchers,
            accordion)


def __generate_card(metadata: dict) -> str:
    return """
        <div class=\"card\">
            <div class=\"card-header\">
                <h5 class="mb-0">
                    <button class=\"btn btn-link\" type=\"button\" data-toggle=\"collapse\" data-target=\"#collapse{0}\" aria-expanded=\"false\" aria-controls=\"collapse{0}\">
                        {1}/{2} <a href=\"{3}\" class=\"fa fa-github\" aria-hidden=\"true\"></a>
                    </button>
                </h5>
            </div>
            <div id=\"collapse{0}\" class=\"collapse\" aria-labelledby=\"heading{0}\" data-parent=\"#accordion\">
                <div class=\"card-body\">
                    <p class=\"font-weight-light\">{4}</p>
                    <span class="badge badge-pill badge-dark">Created at: {5}</span>
                    <span class="badge badge-pill badge-dark">Pushed at: {6}</span><br/>
                    <span class=\"badge badge-pill badge-primary\">Default branch: {7}</span>
                    <span class=\"badge badge-pill badge-danger\">Issues: {8}</span>
                    <span class=\"badge badge-pill badge-success\">Releases: {9}</span>
                    <span class=\"badge badge-pill badge-warning\">Stars: {10}</span>
                    <span class=\"badge badge-pill badge-info\">Watchers: {11}</span>
                    <span class=\"badge badge-pill badge-secondary\">Language: {12}</span>
                </div>
            </div>
        </div>
        """.format(metadata.get('id'),
                   metadata.get('owner'),
                   metadata.get('name'),
                   metadata.get('url'),
                   metadata.get('description'),
                   metadata.get('created_at'),
                   metadata.get('pushed_at'),
                   metadata.get('default_branch'),
                   metadata.get('issues'),
                   metadata.get('releases'),
                   metadata.get('stars'),
                   metadata.get('watchers'),
                   metadata.get('primary_language'))

"""
mined_repos = [{
    'id': 'Test',
    'default_branch': 'master',
    'owner': 'stefano',
    'name': 'my-repo',
    'url': 'none',
    'description': 'this is a description',
    'issues': 4,
    'releases': 10,
    'stars': 1,
    'watchers': 2,
    'primary_language': 'python',
    'continuous_integration': True,
    'percent_comment': 12.00,
    'commit_frequency': 9.00,
    'core_contributors': 3,
    'iac_ratio': 67.00,
    'issue_frequency': 0.023,
    'license': True,
    'repository_size': 190'
}, {
    'id': 'Test2',
    'default_branch': 'master',
    'owner': 'stefano',
    'name': 'my-second-repo',
    'url': 'none',
    'description': 'this is another description',
    'issues': 47,
    'releases': 160,
    'stars': 19,
    'watchers': 29,
    'primary_language': 'python',
    'created_at': '2010-10-23',
    'pushed_at': '2020-08-31',
}]

print(generate_mining_report(mined_repos))
"""