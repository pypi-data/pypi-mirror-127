:tocdepth: 3

.. _plasmapy-documentation:

.. image:: _static/graphic-circular.png
   :alt: PlasmaPy logo
   :align: right
   :scale: 40%

######################
PlasmaPy Documentation
######################

PlasmaPy_ is an open source community-developed core Python_ 3.7+
package for plasma physics currently under development.

Example highlights
------------------

.. nbgallery::
   :hidden:

   notebooks/diagnostics/charged_particle_radiography_particle_tracing
   notebooks/dispersion/two_fluid_dispersion
   notebooks/diagnostics/thomson
   notebooks/analysis/swept_langmuir/find_floating_potential
   notebooks/formulary/thermal_bremsstrahlung
   notebooks/plasma/grids_nonuniform


.. toctree::
   :caption: First Steps
   :maxdepth: 1

   Vision Statement <about/vision_statement>
   Installing <install>
   examples
   COMMUNICATION
   CONTRIBUTING
   CODE_OF_CONDUCT
   about/citation

.. toctree::
   :maxdepth: 1
   :caption: Package features

   ad/index
   Dispersion <dispersion/index>
   Formulary <formulary/index>
   Particles <particles/index>
   Simulation <simulation/index>
   Plasma Objects <plasma/index>
   Package Utilities <utils/index>

.. toctree::
   :maxdepth: 1
   :caption: Guide for Contributors

   Overview <development/index>
   development/code_guide
   development/doc_guide
   development/testing_guide

.. toctree::
   :maxdepth: 1
   :caption: All the Rest

   about/credits
   bibliography
   glossary
   whatsnew/index
   about/stability
   PlasmaPy.org <https://www.plasmapy.org>

.. The about PlasmaPy section has some important information that would
   be helpful to have more readily accessible from the main doc index
   page.

.. TODO: Add feedback link: .. _feedback@plasmapy.org: mailto:feedback@plasmapy.org
