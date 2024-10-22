from flask import Flask, render_template, request
import random

from flask.helpers import url_for
app = Flask(__name__)
"""
2-bromobutane
benzene
butane
ethanal
ethanoic_acid
hex-3-yne
1-methoxypropane
n-methylbutan-2-amine
n_n-dimethylpropanamide
pent-2-ene
pentan-2-one
propan-2-ol
propyl_ethanoate


"""

frontlist=[

'Aristotle',

'Democritus (300 B.C)',

'All matter made up of tiny particles (atoms)',

'Thomson Model of the Atom',

'Calculate relative charge and mass of the electron',

'Ernest Rutherford (1911)',

'Proved the existence of the neutron',

'Neils Bohr',

'Quantum Hypothesis made to explain observations',

'The energy of the photon is transferred to the electron',

'Energy level must be filled before moving up next level',

'Pauli Exclusion Principle',

'Hund’s Rule',

'Ionic Compounds',

'Molecular Compounds',

'What type of bond? ΔEN = 0.2',

'What type of bond? ΔEN = 1.9'
]

backlist=[

'Only four elements earth, air, fire and water',

'Atoms are made of tiny, indivisible things',

'Dalton’s Atomic Theory',

'Electrons could be emitted from matter',

'Robert Millikan (1909)',

'Discovered atom is mostly empty space',

'James Chadwick (1932)',

'The Planetary Model',

'Max Planck (1900)',

'Einstein (1905)',

'Aufbau Principle',

'No 2 e- in an atom can have 4 quantum numbers, on 2 e- can exist per orbital',

'1 e- is placed in each suborbital',

'Made of ionic bonds, usually between metals and nonmetals, bonded in a crystal lattice structure, EN >= 1.7',

'Covalent bonds between 2 nonmetals, EN = 0 to 0.5 is nonpolar',

'Non-polar bond',

'Polar bond'

]

correct='<div class="answer"><h1 class="c">&check;</h1><p class="c">Correct!</p><p>Your answer:</p><p>'
incorrect='<div class="answer"><h1 class="x">&cross;</h1><p class="x">Incorrect!</p><p>Your answer:</p><p>'
style='<style>input{display:none;}.hide{display:none;}</style>'
answerdict={
    'in1.1':'</p><hr/> <p>Correct answer:</p><table class="hct"> <tr> <th>System</th> <th>Surrounding</th> </tr><tr> <td>Metal</td><td>Water</td></tr><tr> <td>m=300g</td><td>m=500g</td></tr><tr> <td>c=?</td><td>c=4.184 J/g°C</td></tr><tr><td>T<sub>1</sub>=915°C</td><td>T<sub>1</sub>=21.5°C</td></tr><tr><td>T<sub>2</sub>=74.6°C</td><td>T <sub>2</sub>=74.6°C</td></tr><tr><td>𝚫T=-840.4°C</td><td>𝚫T=+53.1°C</td></tr></table><div><p>Q=mcT</p><p>Q=(500g)(4.184 J/g°C)(53.1°C)</p><p>Q<sub>water</sub>=111,085.2 J</p><p>Q<sub>metal</sub>=-111,085.2 J</p><p>c=-111,085.2J / (300g)(-840.4°C)</p><p>c=0.44060447 J/g°C</p><p>c=0.4406 J/g°C</p></div></div>',
    'in1.2':'</p><hr/> <p>Correct answer:</p><table class="hct"> <tr> <th>Substance</th> <th>Heat Capacity</th> </tr><tr style="background-color: #6cb400"> <td>Iron</td><td>0.440</td></tr><tr> <td>Lithium</td><td>3.56</td></tr><tr> <td>Sodium</td><td>1.23</td></tr><tr> <td>Aluminum</td><td>0.900</td></tr><tr> <td>Potassium</td><td>0.75</td></tr><tr> <td>Lead</td><td>0.160</td></tr><tr> <td>Gold</td><td>0.1290</td></tr></table> <p>Iron is most likely</p></div>',
    'in2.1':'</p><hr/> <p>Correct answer:</p><p> 2C<sub>6</sub>H<sub>14</sub> + 19O<sub>2</sub> → 12CO<sub >2</sub > + 14H<sub>2</sub>O </p></div>',
    'in2.2':'</p><hr/> <p>Correct answer:</p><p> ΔH=∑[(n)(ΔH<sub>f</sub> Products)] - ∑[(n)(ΔH<sub>f</sub> Reactants)] </p><p> ΔH=[(12 mol)(ΔH<sub>f</sub> CO<sub>2</sub>) + (14 mol)(ΔH<sub >f</sub > H<sub>2</sub>O)] - [(2 mol)(ΔH<sub>f</sub> C<sub>6</sub>H<sub>14</sub>) + (19 mol)(ΔH<sub>f</sub> O<sub>2</sub>)] </p><p> ΔH=[(12 mol)(-393.5 kJ/mol) + (14 mol)(-285.8 kJ/mol)] - [(2 mol)(-198.67 kJ/mol) + <s>(19 mol)(0 kJ/mol)</s>] </p><p>ΔH=[-8723.2 kJ] - [-397.34 kJ]</p><p>ΔH=-8325.86 kJ</p></div>',
    'in2.3':'</p><hr/> <p>Correct answer:</p><p>ΔH=(n)(ΔH<sub>x</sub>)</p><p>ΔH<sub>x</sub>=-8325.86 kJ / 2 mol</p><p>ΔH<sub>x</sub>=-4162.93 kJ/mol</p></div>',
    'in3.1':'</p><hr/> <p>Correct answer:</p><p>ΔS=∑[(n)(ΔS Products)] - ∑[(n)(ΔS Reactants)]</p><p> ΔS=[(2 mol)(ΔS LiOH) + (1 mol)(ΔS H<sub>2</sub>)] - [(2 mol)(ΔS Li) + (2 mol)(ΔS H<sub>2</sub>O)] </p><p>ΔS=[(2 mol)(47.97 J/mol*K) + (1 mol)(130.6  J/mol*K)] - [(2 mol)(ΔS 29.09 J/mol*K) + (2 mol)(69.95 J/mol*K)]</p><p>ΔS=[226.54 J/mol*K] - [198.08 J/mol*K]</p><p>ΔS=28.46 J/mol*K</p></div>',
    'in3.2':'</p><hr/> <p>Correct answer:</p><p>Yes, because the ΔS is positive</p></div>'
}

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/chem12cpt/")
def chem12cpt():
    return render_template("chem12cpt.html")

#UNITS
@app.route("/chem12cpt/unit1/")
def unit1():
    return render_template("unit1.html")

@app.route("/chem12cpt/unit2/")
def unit2():
    f = '<p>ftest</p><p>test</p>'
    b = '<p>btest</p><p>test</p>'
    r = random.randint(0, len(frontlist)-1)
    return render_template("card.html", front=f"<p>{frontlist[r]}</p>", back=f"<p>{backlist[r]}</p>")



@app.route("/chem12cpt/unit3/", methods=["POST","GET"])
def unit3():
    if request.method == "POST":
        in11 = request.form['in1.1']
        in12 = request.form['in1.2']
        in211 = request.form['in2.1.1']
        in212 = request.form['in2.1.2']
        in213 = request.form['in2.1.3']
        in214 = request.form['in2.1.4']
        in22 = request.form['in2.2']
        in23 = request.form['in2.3']
        in31 = request.form['in3.1']
        in32 = request.form['in3.2']
        print(in11)
        print(in211)
        """ 
        for key in a_dict:
            print(key)
        """

        indic={}
        try:
            if float(in11) > 0.43 and float(in11) < 0.45:
                print("correct")
                indic['in1.1']=f"{correct}{in11}{answerdict['in1.1']}"
            else:
                indic['in1.1']=f"{incorrect}{in11}{answerdict['in1.1']}"
        except:
            indic['in1.1']=f"{incorrect}{in11}{answerdict['in1.1']}"

        try:
            if in12.lower() == 'iron':
                indic['in1.2']=f"{correct}{in12}{answerdict['in1.2']}"
            else:
                indic['in1.2']=f"{incorrect}{in12}{answerdict['in1.2']}"
        except:
            indic['in1.2']=f"{incorrect}{in12}{answerdict['in1.2']}"

        try:
            if in211=='2C6H14' and in212=='19O2' and in213=='12CO2' and in214=='14H2O' or in211=='2C6H14' and in212=='19O2' and in213=='14H2O' and in214=='12CO2':
                indic['in2.1']=f"{correct}{in211} + {in212} → {in213}+ {in214}{answerdict['in2.1']}"
            else:
                indic['in2.1']=f"{incorrect}{in211} + {in212} → {in213} + {in214}{answerdict['in2.1']}"
        except:
            indic['in2.1']=f"{incorrect}{in211} + {in212} → {in213} + {in214}{answerdict['in2.1']}"
        
        try:
            if float(in22) > -8400 and float(in22) < -8300:
                indic['in2.2']=f"{correct}{in22} kJ{answerdict['in2.2']}"
            else:
                indic['in2.2']=f"{incorrect}{in22} kJ{answerdict['in2.2']}"
        except:
            indic['in2.2']=f"{incorrect}{in22} kJ{answerdict['in2.2']}"
        try:
            if float(in23) > -4200 and float(in23) < -4100:
                indic['in2.3']=f"{correct}{in23} kJ/mol{answerdict['in2.3']}"
            else:
                indic['in2.3']=f"{incorrect}{in23}  kJ/mol{answerdict['in2.3']}"
        except:
            indic['in2.3']=f"{incorrect}{in23}  kJ/mol{answerdict['in2.3']}"
        try:
            if float(in31) > 27 and float(in31) < 29:
                indic['in3.1']=f"{correct}{in31} J/mol*K{answerdict['in3.1']}"
            else:
                indic['in3.1']=f"{incorrect}{in31} J/mol*K{answerdict['in3.1']}"
        except:
            indic['in3.1']=f"{incorrect}{in31} J/mol*K{answerdict['in3.1']}"
        try:
            if in32.lower() == 'yes':
                indic['in3.2']=f"{correct}{in32}{answerdict['in3.2']}"
            else:
                indic['in3.2']=f"{incorrect}{in32}{answerdict['in3.2']}"
        except:
            indic['in3.2']=f"{incorrect}{in32}{answerdict['in3.2']}"
        #print(in11)
        print(in12)
        return render_template("unit3.html", style=style, testa=indic)
    return render_template("unit3.html")

@app.route("/chem12cpt/unit4/")
def unit4():
    return render_template("unit4.html")



@app.route("/3d/<model>/")
def model(model):
    return render_template("model.html", model=model)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8034)