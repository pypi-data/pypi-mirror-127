PhotoElectrochemistry
======================

Basics
--------------

Photo-electrochemistry characterizations are used to study films at macroscopic, mesoscopic, and microscopic scales. 
The latter advances were used to support (photo-)electrochemical studies of the electronic and optical properties of passive films 
and oxidized metals, and of their interfaces with electrolytes, providing informations on the nature and structure of these 
materials and to use properties such as the oxidation behaviour of a metallic substrate. 

Basically, two kinds of curves are recorded in the course of photoelectrochemical characterization experiments, 
photocurrent voltammograms and photocurrent energy spectra. In photocurrent voltammograms, photocurrents are measured 
as a function of the potential, :math:`V`, applied to the semiconducting electrode, at a given photon energy, :math:`E=h\nu`. 
In photocurrent energy spectra, photocurrents are recorded, at a given applied potential, V, as a function of the photon energy, :math:`E`. 
The analysis of the shapes of photocurrent voltammograms may allow to obtain informations such as the semiconducting type of the material, 
the energy of the surface band levels, the presence of macroscopic defects inducing photogenerated electron--hole pairs recombinations. 

However, despite attempts to refine the Gartner-Butler model by taking into account surface or volume recombination, 
a complete description of the photocurrent voltammograms remains difficult, for the latter developments make use of a 
high number of adjustable parameters, most of them being very difficult to assess. The analysis of the photocurrent 
energy spectra is intended to identify the chemical nature of the material constituting the semiconducting electrode, 
through the value of their bandgap energies, :math:`E_g` as, on the one hand, bandgap energy values have been reported 
in the literature for numerous compounds, and as, on the other hand, bandgap values may be estimated from thermodynamic extensive atomic data. 
Practically, photocurrent energy spectra are usually analyzed by means of linear transforms to take benefit of the fact that, 
using the simplified form of the Gartner--Butler model, the quantum yield, :math:`\eta`, of the photocurrent is proportional 
to the light absorption coefficient. 

In such conditions, :math:`\eta`, obeys to the following relationship:

.. math::
			(\eta * E)^{1/n} = K(E-E_g)

where :math:`C` is a constant (things other than :math:`E` being equal), 
:math:`E_g` is the bandgap energy of the semiconductor, and :math:`n` depends 
on the band to band transition type, :math:`n=1/2` for an allowed direct transition, 
and :math:`n=2` for an allowed indirect transition. Direct transitions are rarely 
observed in more or less disordered thin oxide films. 

Fitting
--------------------------------------------

Linear transformations were successfully performed for oxides made of one or two constituents. 
However, for complex oxide scales formed of several p-type and n-type phases, the complete 
description of the photocurrent energy spectra could not be achieved, and only semi-quantitative 
and/or partial informations could be obtained on the oxides present in the scales. 

As :math:`I_{PH}^{\ast}` is measured under modulated light conditions and thus actually is a complex number, 
the real and the imaginary parts of the photocurrent  should be considered simultaneously when analyzing 
and fitting the photocurrent energy spectra, rather than their modulus :cite:p:`Petit2013`.

.. math::
    :label: eq:complex_iph

            I_{PH}^{\ast}& = \vert I_{PH}^{\ast} \vert \cos \theta
            + j \vert I_{PH}^{\ast} \vert \sin \theta \\
            I_{PH}^{\ast}& = \sum _{i}^{i=N} J_{PH,i} \cos \theta _{i} + j \sum _{i}^{i=N} J_{PH,i} \sin \theta _{i}
			
where :math:`J_{PH,i}` and :math:`\theta _{i}` represent the modulus and phase shift, respectively, 
of the photocurrent issued from the ith semiconducting constituent of the oxide layer. 
For thin semiconducting films, the space charge regions are low compared to penetration depth of the light. 
:math:`J_{PH,i}` may thus be expected, at a given applied potential, to follow the simplified form of the Gartner--Butler model.

.. math::
			(J_{PH,i} * E)^{1/n} = K_{i}(E-E_{g,i})

where :math:`E_{g,i}` and :math:`K_{i}` represent the energy gap and a value proportional 
to :math:`C` (:math:`I_{PH}^{\ast}` * is proportional to but not equal to :math:`\eta`) for the ith semiconducting constituent.


For a given vector of :math:`m` (:math:`K _{i}`, :math:`\theta _{i}`, :math:`E_{g,i}`) triplets, 
:math:`m` representing the supposed number of semiconducting phases contributing to the photocurrent, 
the scalar function to be minimized by the Nelder-Mead function was defined as the product of the square roots of two quantities:

	.. math::
            D_{Re} & = \sqrt{ \sum _{E}(Re I_{PH,exp}^{\ast} - Re I_{PH,calc}^{\ast})^2 } \\
            D_{Im} & = \sqrt{ \sum _{E}(Im I_{PH,exp}^{\ast} - Im I_{PH,calc}^{\ast})^2 }

            D = D_{Re} . D_{Im}

The 3 :math:`m` variables can be locked or not by the user. Initial estimates can be provided by 
the user or can be randomly generated. Several successive calls of the Nelder-Mead procedure are 
necessary to reach the minimum of the scalar function and a stable set of the output parameters. 
The user is free to set the number of successive calls of the Nelder-Mead procedure. 
Constraints on the 3 :math:`m` variables can be set by the user.

    
GUI
====================

The main window contains all the elements necessary to run the fit. The design is cluttered but it allows exposing
directly all the fitting settings to the user without deep menus.


.. figure:: ../images/User_Guide-Global_Overview.png
    :width: 1200
    :align: center


The different steps, presented in the left pane, for performing the fit are:

* load data: the accepted formats are:
   * :ref:`dot_files` files which are ascii files developped in the SiMaP Lab
   * :ref:`data_files` files which are generic ascii files
* set the number of semiconductive contributions (:ref:`parameter_table`)

At this point the fit can be ran. 

If needed select custom choice for all the fitting parameter in the left pane.


.. _dot_files:

\*.dot files
--------------------

They have a specific formating and they are provided by the PEC setup in the SiMaP Lab. 


.. _data_files:

\*.data files
--------------
The \*.data files are generic ascii files where:

* the first column is the energy of the incident light in eV.
* the second column is the modulus of the photocurrent in A.
* the thrid column is the phase shift of the photocurrent in degrees.

.. _parameter_table:

Parameter Table
------------------

The parameter table allows for fitting the *3m* variables. The table is structured as shown below:


====  ========== ============ ================= ======= ============
Ki    Fit Kgi    theta i      Fit Phase i       Egi     Fit Egi
====  ========== ============ ================= ======= ============
K 1   0 or 1     Phase 1       0 or 1           Eg 1    0 or 1
K 2   0 or 1     Phase 2       0 or 1           Eg 2    0 or 1
\...  \...       \...          \...             \...    \...
K n   0 or 1     Phase n       0 or 1           Eg n    0 or 1
====  ========== ============ ================= ======= ============

Each parameter :math:`K_i`, :math:`\theta _i` and :math:`Eg_i` can be locked by setting the **Fit X** column to 0.