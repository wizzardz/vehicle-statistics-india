using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace vsapi.Model
{
    public class StatiticsData
    {
        /// <summary>
        /// Gets or sets the localized value vehicle catagory for display
        /// </summary>
        public string Category
        {
            get
            {
                return GetResourceString(typeof(VehicleCategory), this.VehicleCategory);
            }
        }

        /// <summary>
        /// Gets or sets the type of the vehicle
        /// </summary>
        public VehicleType VehicleType { get; set; }

        /// <summary>
        /// Gets or sets the category of the vehicle
        /// </summary>
        public VehicleCategory VehicleCategory { get; set; }

        /// <summary>
        /// Gets the localized string value corresponds to the vehicle type for display
        /// </summary>
        public string VehicleText
        {
            get
            {
                return GetResourceString(typeof(VehicleType), this.VehicleType);
            }
        }

        /// <summary>
        /// Gets or sets a value that indicates whether the vehicle is Transport or not
        /// </summary>
        public bool IsTransport { get; set; }

        /// <summary>
        /// Gets or sets number of newly registered vehicles
        /// </summary>
        public int Count { get; set; }

        /// <summary>
        /// Gets or sets the evaluation period for the statistic data
        /// </summary>
        public string Period { get; set; }

        /// <summary>
        /// Get the localized string for the specified type and value
        /// </summary>
        /// <param name="enumeratorType">The type of the enumerator</param>
        /// <param name="enumeratorValue">Value of the enumerator</param>
        /// <returns>The localized value of the specified enumerator type</returns>
        private string GetResourceString(Type enumeratorType,object enumeratorValue)
        {
            return VehicleApiResources.ResourceManager.GetString(string.Format("{0}{1}Text", enumeratorType.Name, enumeratorValue));
        }
    }

    public enum State
    {
        AndamanNicorarIslands = 1,
        AndraPredesh = 2,
        Assam = 3,
        Bihar = 4,
        Chandigarh = 5,
        Chhattisgarh = 6,
        DadraNagarHaveli = 7,
        DamanAndDiu = 8,
        Delhi = 9,
        Goa = 10,
        Gujarat = 11,
        Haryana = 12,
        HimachalPradesh = 13,
        JammuKashmir = 14,
        Jharkhand = 15,
        Karnataka = 16,
        Kerala = 17,
        Lakshadweep = 18,
        MadhyaPradesh = 19,
        Maharashtra = 20,
        Manipur = 21,
        Meghalaya = 22,
        Mizoram = 23,
        Nagaland = 24,
        Odisha = 25,
        Puducherry = 26,
        Punjab = 27,
        Rajasthan = 28,
        Sikkim = 29,
        TamilNadu = 30,
        Tripura = 31,
        UttarPradesh = 32,
        Uttarakhand = 33,
        WestBengal = 34
    }

    public enum VehicleCategory
    {
        MAV = 1,
        TL = 2,
        LMVGoods = 3,
        LMVPassengers = 4,
        Bus = 5,
        Taxi = 6,
        MotorCyclesOnHire = 7,
        TwoWheeler = 8,
        Car = 9,
        Jeep = 10,
        OmniBus = 11,
        Tractor = 12,
        Trailer = 13,
        Others = 14
    }

    public enum VehicleType
    {
        MAV = 1,
        TL = 2,
        FourWheeler = 3,
        ThreeWheeler = 4,
        StageCarriage = 5,
        ContractCarriage = 6,
        PrivateServiceVehicle = 7,
        OtherBus = 8,
        MotorCab = 9,
        MaxiCab = 10,
        OtherTaxi = 11,
        ThreeSeater = 12,
        FourSixSeater = 13,
        MotorCycleOnHire = 14,
        Scooter = 15,
        Moped = 16,
        MotorCycle = 17,
        Car = 18,
        Jeep = 19,
        OmniBus = 20,
        Tractor = 21,
        Trailer = 22,
        OtherVehicle = 23
    }
}
