"""Manages topic icons.

Not all topics have icons yet but soon they all will!

Each math topic also has a badge icon (badges/topic_exercise_badges.py), which
can soon be replaced with appropriately-masked hexagonal versions of these.
"""


# When finding an icon for a topic, we look for the topic slug in
# _OVERRIDE_ICONS; failing that we look for the slugs of the topic and the
# topic's ancestors in _ICONS. (For example, we have grade-level subject icons
# but if we're missing a topic icon for a grade-level topic we want to fall
# back to the default math icon, not the subject icon.)
_OVERRIDE_ICONS = {
    'cc-third-grade-math': 'grades/grade-3.png',
    'cc-fourth-grade-math': 'grades/grade-4.png',
    'cc-fifth-grade-math': 'grades/grade-5.png',
    'cc-sixth-grade-math': 'grades/grade-6.png',
    'cc-seventh-grade-math': 'grades/grade-7.png',
    'cc-eighth-grade-math': 'grades/grade-8.png',
}

_ICONS = {
    'math': 'math/arithmetic.png',

    'early-math': 'math/early-math.png',  # subject
    'cc-early-math-counting-topic': 'math/counting.png',
    'cc-early-math-place-value-topic': 'math/place-value.png',
    'cc-early-math-add-sub-topic': 'math/addition-subtraction.png',
    'cc-early-math-measure-data-topic': 'math/measure-data.png',
    'cc-early-math-geometry-topic': 'math/geometry.png',

    'cc-3rd-add-sub-topic': 'math/addition-subtraction.png',
    'cc-3rd-mult-div-topic': 'math/multiplication-division.png',
    'cc-3rd-fractions-topic': 'math/fractions.png',
    'cc-third-grade-measurement': 'math/measure-data.png',
    'cc-3rd-place-value-rounding': 'math/place-value-rounding.png',
    'cc-3rd-exp-pattern-topic': 'math/expressions.png',

    'cc-4th-add-sub-topic': 'math/addition-subtraction.png',
    'cc-4th-mult-div-topic': 'math/multiplication-division.png',
    'cc-4th-fractions-topic': 'math/fractions.png',
    'cc-4th-measurement-topic': 'math/measure-data.png',
    'cc-4th-geometry-topic': 'math/geometry.png',
    'cc-4th-fact-mult-topic': 'math/factors-multiples-patterns.png',
    'cc-5th-place-value-rounding-topi': 'math/place-value-rounding.png',

    'cc-5th-arith-operations': 'math/arithmetic.png',
    'cc-5th-fractions-topic': 'math/fractions.png',
    'cc-5th-place-value-decimals-top': 'math/place-value-decimals.png',
    'cc-5th-measurement-topic': 'math/measure-data.png',
    'cc-5th-geometry-topic': 'math/geometry.png',
    'cc-5th-algebraic-thinking': 'math/algebraic-thinking.png',

    'cc-6th-ratios-prop-topic': 'math/percentages.png',
    'cc-6th-arithmetic-operations': 'math/arithmetic.png',
    'cc-6th-negative-number-topic': 'math/absolute-value.png',
    'cc-6th-factors-and-multiples': 'math/arithmetic.png',
    'cc-6th-geometry-topic': 'math/geometry.png',
    'cc-6th-expressions-and-variables': 'math/expressions.png',
    'cc-6th-data-statistics': 'math/data-statistics.png',

    'cc-7th-ratio-proportion': 'math/rates-and-ratios.png',
    'cc-7th-negative-numbers': 'math/absolute-value.png',
    'cc-7th-fractions-decimals': 'math/fractions-decimals.png',
    'cc-7th-variables-expressions': 'math/expressions.png',
    'cc-7th-geometry': 'math/geometry.png',
    'cc-7th-probability-statistics': 'math/probability.png',

    'cc-8th-relationships-functions': 'math/relationships-functions.png',
    'cc-8th-systems-topic': 'math/systems-of-eq-and-ineq.png',
    'cc-8th-geometry': 'math/geometry.png',
    'cc-8th-data': 'math/data-modeling.png',

    'arithmetic': 'math/arithmetic-subject.png',  # subject
    'addition-subtraction': 'math/addition-subtraction.png',
    'multiplication-division': 'math/multiplication-division.png',
    'factors-multiples': 'math/factors-multiples.png',
    'absolute-value': 'math/absolute-value.png',
    'decimals': 'math/decimals.png',
    'fractions': 'math/fractions.png',
    'rates-and-ratios': 'math/rates-and-ratios.png',
    'applying-math-reasoning-topic': 'math/applying-math-reasoning.png',
    'exponents-radicals': 'math/exponents-radicals.png',
    'order-of-operations': 'math/arithmetic.png',
    'telling-time': 'math/telling-time.png',
    'measurement': 'math/measure-data.png',

    'algebra': 'math/algebra.png',  # subject
    'solving-linear-equations-and-inequalities': 'math/linear-equations.png',
    'linear_inequalities': 'math/linear-inequalities.png',
    'linear-equations-and-inequalitie': 'math/graphing-analyzing-linear.png',
    'systems-of-eq-and-ineq': 'math/systems-of-eq-and-ineq.png',
    'multiplying-factoring-expression':
        'math/multiplying-factoring-expression.png',
    'quadratics': 'math/quadratics.png',
    'exponent-equations': 'math/exponent-equations.png',
    'algebra-functions': 'math/functions.png',
    'ratio-proportion-topic': 'math/rates-and-ratios.png',

    'geometry': 'math/geometry-subject.png',  # subject
    'intro_euclid': 'math/intro-euclid.png',
    'parallel-and-perpendicular-lines': 'math/angles.png',
    'congruent-triangles': 'math/congruence.png',
    'similarity': 'math/similarity.png',
    'right_triangles_topic': 'math/right-triangles.png',
    'basic-geometry': 'math/perimeter-area-volume.png',
    'cc-geometry-circles': 'math/circles.png',
    'triangle-properties': 'math/triangle-properties.png',
    'quadrilaterals-and-polygons': 'math/quadrilaterals.png',
    'transformations': 'math/transformations.png',
    'analytic-geometry-topic': 'math/analytic-geometry.png',
    'geometric-constructions': 'math/geometric-constructions.png',

    'algebra2': 'math/algebra-ii.png',  # subject
    'systems_eq_ineq': 'math/systems-of-eq-and-ineq.png',
    'functions_and_graphs': 'math/functions-and-graphs.png',
    'polynomial_and_rational': 'math/polynomial-and-rational.png',
    'rational-expressions': 'math/rational-expressions.png',
    'exponential_and_logarithmic_func': 'math/exponential-logarithmic.png',
    'logarithms-tutorial': 'math/logarithms.png',
    'complex-numbers-a2': 'math/imaginary.png',
    'conics_precalc': 'math/conics.png',
    'algebra-matrices': 'math/matrices.png',

    'trigonometry': 'math/trigonometry.png',  # subject
    'unit-circle-trig-func': 'math/unit-circle.png',
    'trig-function-graphs': 'math/trig-graphs.png',
    'less-basic-trigonometry': 'math/trig-identities.png',

    'probability': 'math/probability.png',  # subject
    'independent-dependent-probability': 'math/independent-dependent.png',
    'probability-and-combinatorics-topic': 'math/combinatorics.png',
    'descriptive-statistics': 'math/descriptive-statistics.png',
    'random-variables-topic': 'math/random-variables.png',
    'regression': 'math/regression.png',
    'statistics-inferential': 'math/inferential-statistics.png',

    'precalculus': 'math/precalculus.png',  # subject
    'vectors-precalc': 'math/vectors.png',
    'parametric_equations': 'math/parametric.png',
    'imaginary_complex_precalc': 'math/imaginary.png',
    'prob_comb': 'math/probability.png',
    'seq_induction': 'math/sequences.png',
    'hyperbolic_trig_topic': 'math/hyperbolic.png',
    'limit_topic_precalc': 'math/limits.png',

    'differential-calculus': 'math/differential-calculus.png',  # subject
    'limits_topic': 'math/limits.png',
    'taking-derivatives': 'math/taking-derivatives.png',
    'derivative_applications': 'math/derivative-applications.png',

    'integral-calculus': 'math/integral-calculus.png',  # subject
    'indefinite-definite-integrals': 'math/definite-integrals.png',
    'solid_revolution_topic': 'math/solids-of-revolution.png',
    'sequences_series_approx_calc': 'math/sequences-calc.png',
    'ap_calc_topic': 'math/ap.png',

    'multivariable-calculus': 'math/multivariable-calculus.png',  # subject
    'double_triple_integrals': 'math/double-triple-integrals.png',
    'partial_derivatives_topic': 'math/partial-derivatives.png',
    'line_integrals_topic': 'math/line-integrals.png',
    'surface-integrals': 'math/surface-integrals.png',
    'divergence_theorem_topic': 'math/divergence-theorem.png',

    'differential-equations': 'math/diff-equations.png',  # subject
    'first-order-differential-equations':
        'math/first-order-diff-equations.png',
    'second-order-differential-equations':
        'math/second-order-diff-equations.png',
    'laplace-transform': 'math/laplace-transform.png',

    'linear-algebra': 'math/linear-algebra.png',  # subject
    'vectors_and_spaces': 'math/vectors-spaces.png',
    'matrix_transformations': 'math/matrix-transformations.png',
    'alternate_bases': 'math/alternate-bases.png',

    'recreational-math': 'math/recreational-math.png',  # subject
    'vi-hart': 'math/doodling-in-math.png',
    'brain-teasers': 'math/brain-teasers.png',
    'math-warmup': 'math/math-warmups.png',

    'amc-10': 'math/amc10.png',
    'aime': 'math/aime.png',

    ###

    'science': 'science/chemistry.png',

    'biology': 'science/biology.png',  # subject
    'evolution-and-natural-selection': 'science/evolution.png',
    'cell-division': 'science/cells.png',
    'heredity-and-genetics': 'science/dna.png',
    'tree-of-life': 'science/tree-of-life.png',
    'cellular-respiration': 'science/atp.png',
    'photosynthesis': 'science/photosynthesis.png',
    'human-biology': 'science/human-biology.png',
    'immunology': 'science/immunology.png',
    'crash-course-biology-science': 'science/crash-course.jpg',
    'crash-course-ecology-2': 'science/crash-course.jpg',

    'physics': 'science/physics.png',  # subject
    'one-dimensional-motion': 'science/one-dimensional-motion.png',
    'two-dimensional-motion': 'science/two-dimensional-motion.png',
    'forces-newtons-laws': 'science/newtons-laws.png',
    'work-and-energy': 'science/work-energy.png',
    'linear-momentum': 'science/linear-momentum.png',
    'torque-angular-momentum': 'science/torque.png',
    'newton-gravitation': 'science/gravitation.png',
    'oscillatory-motion': 'science/oscillatory-motion.png',
    'fluids': 'science/fluids.png',
    'thermodynamics': 'science/thermodynamics.png',
    'electricity-and-magnetism': 'science/electricity.png',
    'waves-and-optics': 'science/waves.png',

    'chemistry': 'science/chemistry.png',  # subject
    'introduction-to-the-atom': 'science/atom.png',
    'orbitals-and-electrons': 'science/orbitals-electrons.png',
    'periodic-table-trends-bonding': 'science/periodic-table.png',
    'chemical-reactions-stoichiometry': 'science/chemical-reactions.png',
    'ideal-gas-laws': 'science/ideal-gas-laws.png',
    'states-of-matter': 'science/states-of-matter.png',
    'reaction-rates': 'science/reaction-rates.png',
    'acids-and-bases': 'science/acids-bases.png',
    'oxidation-reduction': 'science/oxidation-reduction.png',
    'radioactive-decay': 'science/radioactive.png',

    'organic-chemistry': 'science/organic-chemistry.png',  # subject
    'gen-chem-review': 'science/general-chemistry.png',
    'organic-structures': 'science/organic-structures.png',
    'bond-line-structures-alkanes-cycloalkanes': 'science/alkanes.png',
    'stereochemistry-topic': 'science/stereochemistry.png',
    'substitution-elimination-reactions':
        'science/substitution-elimination-reactions.png',
    'alkenes-alkynes': 'science/alkenes-alkynes.png',
    'alcohols-ethers-epoxides-sulfides':
        'science/alcohols-ethers-epoxides-sulfides.png',
    'conjugation-diels-alder-mo-theory':
        'science/conjugation-diels-alder-mo-theory.png',
    'aromatic-compounds': 'science/aromatic-compounds.png',
    'aldehydes-ketones': 'science/aldehydes-ketones.png',
    'carboxylic-acids-derivatives': 'science/carboxylic-acids.png',
    'amines-topic': 'science/amines.png',

    'cosmology-and-astronomy': 'science/cosmology-astronomy.png',  # subject
    'universe-scale-topic': 'science/universe-scale.png',
    'stellar-life-topic': 'science/stellar-life.png',
    'earth-history-topic': 'science/earth-history.png',
    'life-earth-universe': 'science/life-on-earth.png',

    'health-and-medicine': 'science/health.png',  # subject
    'MCAT-competition': 'science/mcat.png',
    'circulatory-system': 'science/circulatory-system.png',
    'circulatory-system-diseases': 'science/circulatory-system-diseases.png',
    'respiratory-system': 'science/respiratory-system.png',
    'respiratory-system-diseases': 'science/respiratory-system-diseases.png',
    'renal-system': 'science/renal-system.png',
    'nervous-system-and-sensory-infor': 'science/nervous-system.png',
    'executive systems of the brain': 'science/brain.png',
    'hematologic system': 'science/hematologic-system.png',
    'immune-system': 'science/immune-system.png',
    'musculoskeletal system': 'science/musculoskeletal-system.png',
    'endocrine system': 'science/endocrine-system.png',
    'lab-values': 'science/lab-values.png',
    'endocrinology-and-diabetes': 'science/endocrinology-and-disabetes.png',
    'colon-disease': 'science/colon-disease.png',
    'cervical-spine': 'science/cervical-spine.png',
    'healthy-lifestyle': 'science/healthy-lifestyle.png',
    'health-care-system': 'science/health-care-system.png',
    'healthcare-misc': 'science/health-miscellaneous.png',

    'discoveries-projects': 'science/discoveries-projects.jpg',  # subject
    'discoveries': 'science/discoveries.jpg',
    'Reverse-Eng': 'science/reverse-engineering.jpg',
    'robots': 'science/robots.jpg',
    'lego robotics': 'science/lego-robotics.jpg',
    'Projectile_launcher': 'science/projectile-launcher.jpg',
    'thermo-can': 'science/thermo-can.jpg',
    'simple-machines-explorations': 'science/simple-machines-explorations.jpg',
    'discovery-lab-2013': 'science/discovery-lab-2013.jpg',
    'Discovery-Lab-2012': 'science/discovery-lab-2012.jpg',

    ###

    'microeconomics': 'economics-finance/microeconomics.png',
    'supply-demand-equilibrium': 'economics-finance/supply-demand.png',
    'elasticity-tutorial': 'economics-finance/elasticity.png',
    'consumer-producer-surplus':
        'economics-finance/consumer-producer-surplus.png',
    'choices-opp-cost-tutorial': 'economics-finance/scarcity.png',
    'firm-economic-profit': 'economics-finance/production-decisions.png',
    'perfect-competition-topic': 'economics-finance/forms-of-competition.png',
    'nash-equilibrium-tutorial': 'economics-finance/game-theory.png',

    'macroeconomics': 'economics-finance/macroeconomics.png',
    'gdp-topic': 'economics-finance/gdp.png',
    'inflation-topic': 'economics-finance/inflation.png',
    'aggregate-supply-demand-topic':
        'economics-finance/aggregate-demand-supply.png',
    'monetary-system-topic': 'economics-finance/monetary-system.png',
    'income-and-expenditure-topic': 'economics-finance/income-expenditure.png',
    'forex-trade-topic': 'economics-finance/foreign-exchange.png',

    'core-finance': 'economics-finance/finance-capital-markets.png',
    'interest-tutorial': 'economics-finance/interest-debt.png',
    'housing': 'economics-finance/housing.png',
    'inflation-tutorial': 'economics-finance/inflation.png',
    'taxes-topic': 'economics-finance/taxes.png',
    'accounting-and-financial-stateme': 'economics-finance/accounting.png',
    'stock-and-bonds': 'economics-finance/stocks-bonds.png',
    'investment-vehicles-tutorial':
        'economics-finance/insurance-retirement.png',
    'money-and-banking': 'economics-finance/money-banking.png',
    'derivative-securities': 'economics-finance/options-swaps.png',
    'current-economics': 'economics-finance/current-economics.png',

    'entrepreneurship2': 'economics-finance/entrepreneurship.jpg',

    ###

    'history': 'humanities/history.jpg',
    'euro-hist': 'humanities/1900-present.jpg',
    '1600s-1800s': 'humanities/1700-1900.jpg',
    '1500-1600-Renaissance-Reformation':
        'humanities/renaissance-reformation.jpg',
    'ancient-medieval': 'humanities/ancient-medieval.jpg',
    'history-survey': 'humanities/surveys-of-history.jpg',
    'CrashCourse-WorldHistory': 'humanities/crash-course-world-history.jpg',

    'art-history': 'humanities/art-history.jpg',
    'art-history-400-c-e--ancient-cultures-1': 'humanities/art--400ce.jpg',
    'art-history-400-1300-medieval---byzantine-eras':
        'humanities/art-400-1300.jpg',
    'art-history-1300-1400-proto-renaissance':
        'humanities/art-1300-1400.jpg',
    'art-history-1400-1500-renaissance-in-italy-and-the-north':
        'humanities/art-1400-1500.jpg',
    'art-history-1500-1600-end-of-the-renaissance-and-the-reformation':
        'humanities/art-1500-1600.jpg',
    'art-history-1600-1700-the-baroque': 'humanities/art-1600-1700.jpg',
    'art-history-1700-1800-age-of-enlightenment':
        'humanities/art-1700-1800.jpg',
    'art-history-1800-1848-industrial-revolution-i':
        'humanities/art-industrial-revolution-i.jpg',
    'art-history-1848-1907-industrial-revolution-ii':
        'humanities/art-industrial-revolution-ii.jpg',
    'art-history-1907-1960-age-of-global-conflict':
        'humanities/art-age-of-global-conflict.jpg',
    'art-history-1960---age-of-post-colonialism':
        'humanities/art-age-of-post-colonialism.jpg',

    'american-civics-subject': 'humanities/american-civics.png',

    ###

    'sat': 'test-prep/sat.png',
    'sat-math-practice': 'test-prep/sat-math.png',
    'sat-reading-writing-practice': 'test-prep/sat-reading-writing.png',

    'mcat': 'test-prep/mcat.png',
    'biomolecules': 'test-prep/biomolecules.png',
    'cells': 'test-prep/cells.png',
    'organ-systems': 'test-prep/organ-systems.png',
    'physical-processes': 'test-prep/physical-processes.png',
    'chemical-processes': 'test-prep/chemical-processes.png',
    'processing-the-environment': 'test-prep/processing-environment.png',
    'behavior': 'test-prep/behavior.png',
    'individuals-and-society': 'test-prep/individuals-society.png',
    'society-and-culture': 'test-prep/society-culture.png',

    'gmat': 'test-prep/gmat.png',
    'problem-solving': 'test-prep/problem-solving.png',
    'data-sufficiency': 'test-prep/data-sufficiency.png',

    'cahsee-subject': 'test-prep/cahsee.png',

    'iit-jee-subject': 'test-prep/iit-jee.png',

    'ap-art-history': 'test-prep/ap.png',

    'NCLEX-RN': 'test-prep/nclex-rn.png',
    'nclex-rn-circulatory-system': 'test-prep/circulatory-system.png',
    'rn-cardiovascular-diseases': 'test-prep/circulatory-system-diseases.png',
    'rn-respiratory-system': 'test-prep/respiratory-system.png',
    'rn-respiratory-system-diseases': 'test-prep/respiratory-disease.png',
    'hematologic-system-diseases': 'test-prep/hematologic-disease.png',
    'rn-endocrine-system': 'test-prep/endocrine-system.png',
    'rn-lymphatic-system': 'test-prep/lymphatic-system.png',
    'rn-immune-system': 'test-prep/immune-system.png',
    'rn-renal-system': 'test-prep/renal-system.png',
    'rn-gastrointestinal-system': 'test-prep/gastrointestinal-system.png',
    'rn-muscular-system': 'test-prep/muscular-system.png',
    'rn-skeletal-system': 'test-prep/skeletal-system.png',

    ###

    'college-admissions': 'default/wrapping-up.png',
    'get-started': 'default/get-started.png',
    'making-high-school-count': 'default/making-high-school-count.png',
    'explore-college-options': 'default/explore-college-options.png',
    'applying-to-college': 'default/applying-to-college.png',
    'paying-for-college': 'default/paying-for-college.png',
    'wrapping-up': 'default/wrapping-up.png',
}


def get_icon_for(topic, ancestors):
    # topic is a topic['slug']
    icon_name = _OVERRIDE_ICONS.get(topic)

    if not icon_name:
        # Prefer the icon for the topic itself, but if none exists, use the
        # subject (or failing that, domain) icon
        for t in [topic] + ancestors:
            # TODO(alpert): Match on t.alternate_slug as well?
            icon_name = _ICONS.get(t)
            if icon_name:
                break

    if icon_name:
        path = '/images/topic-icons/%s' % icon_name
        return path
