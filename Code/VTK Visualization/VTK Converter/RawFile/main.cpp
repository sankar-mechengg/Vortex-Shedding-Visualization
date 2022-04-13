// Convert to suitable output format readable by my iso surface plotting code

/*NOTE: ensure that the filenames are in the following format
flow_tXXXX.data where X represents time step numbers. For ex: if time step is 8 second then flow_t0008.data is the filename
Absolutely no error-checking has been implemented so be careful about the filename
*/

#include <fstream>
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <vector>
#include <cmath>

using namespace std;

/*helper function to split input filename*/
vector<string> split(const string& s, char delim)
{
	vector<string> result;
	stringstream ss(s);
	string item;

	while (getline(ss, item, delim)) {
		result.push_back(item);
	}

	return result;
}

int main()
{
	string sourcepath = "D:/Sync Drives/OneDrive - Indian Institute of Science/TWD/E0271_Project/Model_Files/DataFiles/";
	string destpath = "vtkoutputfiles/";

	for (int ti = 8; ti <= 4048; ti += 120)
	{
		//Input from the User
		string sourceFile, destVTKFile;
		string flowfileprefixname = "flow_t";
		string timename = to_string(ti);
		string extension = ".data";
		string vtkextension = ".vtk";
		string threezeros = "000";
		string twozeros = "00";
		string onezero = "0";

		if (ti / 10 == 0)
		{
			sourceFile = flowfileprefixname + threezeros + timename + extension;
			destVTKFile = flowfileprefixname + threezeros + timename + vtkextension;
		}
		else if (ti / 100 == 0)
		{
			sourceFile = flowfileprefixname + twozeros + timename + extension;
			destVTKFile = flowfileprefixname + twozeros + timename + vtkextension;
		}
		else if (ti / 1000 == 0)
		{
			sourceFile = flowfileprefixname + onezero + timename + extension;
			destVTKFile = flowfileprefixname + onezero + timename + vtkextension;
		}
		else
		{
			sourceFile = flowfileprefixname + timename + extension;
			destVTKFile = flowfileprefixname + timename + vtkextension;
		}


		//--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--


		//split source file using '_' as delimiter to get the time step and type of data
		vector<string> params = split(sourceFile, '_');
		string flow = params[0]; //flow
		string timestepdata = params[1]; //tXXXX.data

		//remove the .data extension
		vector<string> format = split(timestepdata, '.');
		string timet = format[0]; //tXXXX

		//remove the t
		vector <string> timevalue = split(timet, 't');
		string time = timevalue[1];


		//--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--

		//calculate the size of the data
		int x = 192, y = 64, z = 48;
		int size = x * y * z;

		ifstream inDataFile;
		ofstream outVTKFile;

		//--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--


		vector<unsigned int> vertices;
		struct vector3ui {
			unsigned int xui, yui, zui;
		};
		vector3ui verticesXYZ;

		for (int i = 0; i < x; i++)
		{
			verticesXYZ.zui = i;
			for (int j = 0; j < y; j++)
			{
				verticesXYZ.yui = j;
				for (int k = 0; k < z; k++)
				{
					verticesXYZ.xui = k;
					vertices.push_back(verticesXYZ.xui);
					vertices.push_back(verticesXYZ.yui);
					vertices.push_back(verticesXYZ.zui);
				}
			}
		}

		std::cout << "The total Number of Individual Vertices: " << vertices.size() << endl;
		std::cout << "The total Number of Vertices: " << vertices.size() / 3 << endl;

		outVTKFile.open(destpath + destVTKFile, ios::out);
		outVTKFile << "# vtk DataFile Version 4.2" << endl;
		outVTKFile << "Flow" << time << endl;
		outVTKFile << "ASCII" << endl;
		outVTKFile << "DATASET STRUCTURED_POINTS" << endl;
		outVTKFile << "DIMENSIONS" << " " << x << " " << y << " " << z << endl;
		outVTKFile << "ORIGIN 0 0 0" << endl;
		outVTKFile << "SPACING 1 1 1" << endl;
		outVTKFile << "POINT_DATA" << " " << size << endl;
		outVTKFile << "VECTORS data float" << endl;



		//--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--


		//open the raw file to read it's contents
		inDataFile.open(sourcepath + sourceFile, ios::in);
		if (!inDataFile.is_open()) {
			std::cout << " Failed to open the File: " << sourcepath + sourceFile << endl;
			return 0;
		}

		float u, v, w, mag;

		int counter = 0;
		for (int i = 0; i < size; i++)
		{
			inDataFile >> u >> v >> w;
			counter++;
			if ((int)(u * 10000) == 0)
			{
				u = 0;
			}
			if ((int)(v * 10000) == 0)
			{
				v = 0;
			}
			if ((int)(w * 10000) == 0)
			{
				w = 0;
			}
			outVTKFile << u << " " << v << " " << w << "\n";	
		}

		std::cout << ti << " - " << counter << endl << endl;

		outVTKFile.close();
		inDataFile.close();

	}

	std::cout << endl << "Data File Converted to VTK Successfully into Text File" << endl << "-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x" << endl;


	return 0;

	//--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x
}