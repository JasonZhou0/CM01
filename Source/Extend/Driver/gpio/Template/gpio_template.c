/*!
 * \addtogroup gpio initialization
 * \{
 *
 * \file        gpio.c
 *
 * \brief       gpio initialization configuration implementation.
 *              The file gpio.c is generated from gpio_template.c.
 *              Do not edit the generated file!
 *
 * Copyright (c) 2018 Jason Zhou
 *
 * All rights reserved. Property of Jason Zhou.
 * Restricted rights to use, duplicate or disclose this code
 * are granted through contract.
 *
 * \}
 */

/* **** Includes **** */

#include "gpio.h"


/* **** Defines **** */

/* **** Typedefs **** */

struct gpio_initializationFuctionStructType_TAG
{
   void* OpFunc;
   const u8 IN_OUT;
   const u8 PULL_DROP;
   const u8 SET_RESET;
};
typedef gpio_initializationFuctionStructType_TAG gpio_initializationFuctionStructType;

/* **** Static Function Declarations **** */

/* **** Static Variables **** */

/* **** Global Variables **** */
const gpio_initializationFuctionStructType initializationFuctionStruct[]=
{
   /*            OpFunc,             IN_OUT, PULL_DROP, SET_RESET    */
% SetNowSheetName('function')
% SetNowSubscript(0)
% for i in range(len(excel.ExcelDict[GetNowSheetName()]['GPIOx'])):
%    SetNowSubscript(i)
   {(void*)gpio_${GPIOx}_${PINx}Init,\t${IN_OUT},\t${PULL_DROP},\t${SET_RESET}},
%end of for
}
/* **** Static Function Definitions **** */

/* **** Function Definitions **** */
% SetNowSheetName('function')
% SetNowSubscript(0)
% for i in range(len(excel.ExcelDict[GetNowSheetName()]['GPIOx'])):
%    SetNowSubscript(i)
/**********************************************************************************************************************
 *
 * Runnable Entity Name: gpio_${GPIOx}_${PINx}Init
 *
 * This runnable can be invoked concurrently (reentrant implementation).
 *
 *---------------------------------------------------------------------------------------------------------------------
 *
 * Executed if at least one of the following trigger conditions occurred:
 *   - triggered by server invocation for OperationPrototype <gpio_${GPIOx}_${PINx}Init> of PortPrototype <???>
 *
 **********************************************************************************************************************
 *
 * Runnable prototype:
 * ===================
 *   Std_ReturnType Dcm_ResetToDefaultSession(void)
 *
 **********************************************************************************************************************
 *
 * Available Application Errors:
 * =============================
 *   RTE_E_DCMServices_E_OK
 *
 *********************************************************************************************************************/
/**********************************************************************************************************************
 * DO NOT CHANGE THIS COMMENT!           << Start of documentation area >>                  DO NOT CHANGE THIS COMMENT!
 * Symbol: ResetToDefaultSession_doc
 *********************************************************************************************************************/


/**********************************************************************************************************************
 * DO NOT CHANGE THIS COMMENT!           << End of documentation area >>                    DO NOT CHANGE THIS COMMENT!
 *********************************************************************************************************************/

void gpio_${GPIOx}_${PINx}Init(void)
{
/**********************************************************************************************************************
 * DO NOT CHANGE THIS COMMENT!           << Start of runnable implementation >>             DO NOT CHANGE THIS COMMENT!
 * Symbol: Dcm_ResetToDefaultSession (returns application error)
 *********************************************************************************************************************/
   
   
   
/**********************************************************************************************************************
 * DO NOT CHANGE THIS COMMENT!           << End of runnable implementation >>               DO NOT CHANGE THIS COMMENT!
 *********************************************************************************************************************/
}
%end of for
