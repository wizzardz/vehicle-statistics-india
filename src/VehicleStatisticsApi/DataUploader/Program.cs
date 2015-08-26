using MongoDB.Bson;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using vsapi.Model;

namespace DataUploader
{
    class Program
    {
        /// <summary>
        /// The variable that holds the instance of mongodb client
        /// </summary>
        private static MongoClient _mongodbClient;

        /// <summary>
        /// The variable that holds the instance of mongodb database currently being used
        /// </summary>
        private static IMongoDatabase _mongodbDatabase;

        /// <summary>
        /// The static constructor which will initialises the mongodb database
        /// </summary>
        static Program()
        {
            Console.WriteLine("Initializing the MongoDB database");
            Console.WriteLine(string.Format("Connection string used :- {0}", ConfigurationManager.ConnectionStrings["MongoDBConnectionString"].ConnectionString));

            try
            {
                _mongodbClient = new MongoClient(ConfigurationManager.ConnectionStrings["MongoDBConnectionString"].ConnectionString);
                _mongodbDatabase = _mongodbClient.GetDatabase("VehicleStatitics");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error occured while initializing the database.");
                Console.WriteLine(e.Message);
            }

            Console.WriteLine("Initialised database successfully.");
        }

        static void Main(string[] args)
        {
            AddOrUpdateStates();
            AddOrUpdateVehicleCategory();
            AddOrUpdateVehicleType();


            Console.ReadLine();
        }

        private static void AddOrUpdateVehicleDataSet()
        {

        }

        /// <summary>
        /// This function which will add/ update the values of the states
        /// </summary>
        private static void AddOrUpdateStates()
        {
            Console.WriteLine("TASK 1: Initialising state values");

            FillEnumeratorValues(typeof(State), "States");

            Console.WriteLine("TASK 1: Completed");
        }

        /// <summary>
        /// The function which will add or update the value of vehicle category
        /// </summary>
        private static void AddOrUpdateVehicleCategory()
        {
            Console.WriteLine("TASK 2: Initialising Vehicle category");

            FillEnumeratorValues(typeof(VehicleCategory), "VehicleCategories");

            Console.WriteLine("TASK 2: Completed");
        }

        /// <summary>
        /// The function which will add or update the value of vehicle types
        /// </summary>
        private static void AddOrUpdateVehicleType()
        {
            Console.WriteLine("TASK 3: Initialising Vehicle types");

            FillEnumeratorValues(typeof(VehicleType), "VehicleTypes");

            Console.WriteLine("TASK 3: Completed");
        }

        private static void FillEnumeratorValues(Type enumeratorType, string collectionName)
        {
            // get the current collection of data avaliable in the states data base
            IMongoCollection<BsonDocument> documentInDatabase = _mongodbDatabase.GetCollection<BsonDocument>(collectionName);

            // get the total number of ducuments currently present in the database
            Task<long> countTask = documentInDatabase.CountAsync(new BsonDocument());
            countTask.Wait();

            // check whether there are any documents returned from the database
            if (countTask.Result == 0)
            {
                Console.WriteLine("No '" + collectionName + "' data is avaliable.");
                Console.WriteLine("Inserting state data");

                List<BsonDocument> documents = new List<BsonDocument>();

                foreach (var enumItem in Enum.GetValues(enumeratorType))
                {
                    Dictionary<string, object> documentValues = new Dictionary<string, object>();
                    documentValues["Name"] = enumItem.ToString();
                    documentValues["Value"] = (int)enumItem;

                    documents.Add(new BsonDocument(documentValues));
                }

                documentInDatabase.InsertManyAsync(documents);

                Console.WriteLine("Completed adding the " + collectionName + " details to the database");
            }
        }
    }
}
