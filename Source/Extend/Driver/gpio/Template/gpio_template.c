// % from automatic import SetNowSheetName
// % from automatic import SetNowSubscript
/*!
 * \addtogroup DTC DTC Handler
 * \{
 *
 * \file        dtc_cfg.c
 *
 * \brief       DTC Handler configuration implementation.
 *              The file dtc_cfg.c is generated from dtc_cfg.template.c.
 *              Do not edit the generated file!
 *
 * Copyright (c) 2017 Autoliv Electronics AB
 *
 * All rights reserved. Property of Autoliv Electronics AB.
 * Restricted rights to use, duplicate or disclose this code
 * are granted through contract.
 *
 * \}
 */

/* **** Includes **** */

#include "gpio.h"


/* **** Defines **** */

/* **** Typedefs **** */

/* **** Static Function Declarations **** */

/* **** Static Variables **** */

/* **** Global Variables **** */

/*! \qacexception 3120: Hard-coded 'magic' integer constant. */
/* PRQA S 3120 ++ */




/* PRQA S 3120 -- */

% i=0
% i-=1
% SetNowSheetName('function')
% SetNowSubscript(0)
// % while (i):
void gpio_${GPIOx}_${PINx}Init(void)
{
   
   
   
   
}
%end of while



/* **** Static Function Definitions **** */

/* **** Function Definitions **** */