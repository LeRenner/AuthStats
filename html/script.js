document.getElementById('NaN').innerHTML = countryStats.NaN

const keys = Object.keys(countryStats).filter(key => key != 'NaN')

function createCountry(key) {
    const tr = document.createElement('tr')
    tr.appendChild(document.createElement('td'))
    tr.appendChild(document.createElement('td'))

    tr.children[0].innerHTML = key
    tr.children[1].innerHTML = countryStats[key]
    tr.children[1].className = "number"
    return tr
}

keys.forEach(key => document.getElementById('countries').appendChild(
    createCountry(key)
))
