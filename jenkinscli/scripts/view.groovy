import jenkins.model.*

def jenkins = Jenkins.instance
def view = jenkins.getView('toolchain')

println "View: ${view.name}"

view.items.each {
    println "Job:${it.name}"
}